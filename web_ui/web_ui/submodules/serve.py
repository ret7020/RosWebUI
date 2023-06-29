from flask import Flask, request
from .items import Page
from std_msgs.msg import String

class App:
    def __init__(self, node) -> None:
        self.flask_app = Flask(__name__, template_folder="../templates", static_folder="../static")
        self.pages = []
        self.node = node

        @self.flask_app.route("/api/topic/pub", methods=['POST'])
        def __api_topic_pub():
            return self.api_topic_pub(request.json)

    
    def api_topic_pub(self, data):
        send = String()
        send.data = data["value"]
        temp_publsiher = self.node.create_publisher(String, data["topic"], 1)
        temp_publsiher.publish(send)
        self.node.destroy_subscription(temp_publsiher)
        return ""

    def add(self, page: Page) -> None:
        '''
        Add page to app
        '''
        self.pages.append(page)
        self.flask_app.add_url_rule(page.path, page.path, page.render)
    
    def start(self) -> None:
        self.flask_app.run()

# @app.route("/")
# def home():
#     page = Page("/", "Abb")
#     page.add(
#         ButtonsGroup([
#             Button("Test"),
#             Button("Test"),
#             Button("Test", "secondary"),
#             Link("Link")
#         ]),
#     )
#     return render_template("base.html", title=page.title, content=page.render())

# if __name__ == "__main__":
#     app.run(debug=True)