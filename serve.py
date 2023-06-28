from flask import Flask
from items import Page

class App:
    def __init__(self) -> None:
        self.flask_app = Flask(__name__)
        self.pages = []

    def add(self, page: Page) -> None:
        '''
        Add page to app
        '''
        self.pages.append(page)

        self.flask_app.add_url_rule(page.path, page.path, page.render)
    
    def start(self) -> None:
        self.flask_app.run(debug=True)

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