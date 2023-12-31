from web_ui.web_ui.serve import App
from web_ui.web_ui.items import Page, ButtonsGroup, Button, Link

app = App()

index = Page("Index test")
index.add(
    ButtonsGroup([
        Button("Test"),
        Button("Test"),
        Button("Test", "secondary"),
        Link("Link")
    ])
)

test_page = Page("Test page", "/test")
test_page.add(
    ButtonsGroup([
        Button("Test"),
        Button("Test"),
        Button("Test"),
        Button("Test"),
        Button("Test"),
        Button("Test"),
        Button("Test"),
        Button("Test"),
        Button("Test"),
        Button("Test")
    ])
)


app.add(index)
app.add(test_page)

app.start()