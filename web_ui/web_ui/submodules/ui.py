from .items import Page, Button

def build(app):
    index_page = Page("Index page", "/")
    index_page.add(
        Button("Nothing button"),
        Button("Actionable button", action="event", topic="/test_topic")
    )
    app.add(index_page)