from flask import Flask, request
from .items import Page
import logging

class App:
    def __init__(self) -> None:
        self.flask_app = Flask(__name__, template_folder="../templates", static_folder="../static")
        self.pages = []

        @self.flask_app.route("/api/topic/pub", methods=['POST'])
        def __api_topic_pub():
            data = request.json()
            logging.error(f"{data}")
            return ""

    
    def api_topic_pub(self):
        pass

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