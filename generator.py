from flask import Flask, render_template
from typing import List

class PageGenerator:
    def __init__():
        pass


class Button:
    def __init__(self, text: str, type_: str="primary", style: str="", href: str="") -> None:
        self.type = type_
        self.text = text
        self.style = style

        # Prepare for render
        bs5_prefix = f"btn-"
        if self.style: bs5_prefix = f"{bs5_prefix}{style}-"
        self.bs5_type = f"{bs5_prefix}{self.type}"

    def render(self):
        return render_template("button.html", button=self.json())
    
    def json(self):
        return {
            "type": self.bs5_type,
            "text": self.text
        }
    
    def __str__(self) -> str:
        return self.render()

class Link(Button):
    def __init__(self, text: str) -> None:
        super().__init__(text, "link", "")

class ButtonsGroup:
    SIZE_MAP = {
        "large": "btn-group-lg",
        "normal": "", # No extra class required
        "small": "btn-group-sm"
    }
    def __init__(self, buttons: List[Button], direction: str="horizontal", size: str = "normal") -> None:
        self.buttons = buttons
        self.size = size

        # Prepare for render
        self.bs5_classes = ButtonsGroup.SIZE_MAP[self.size]

    def render(self):
        return render_template("button_group.html", buttons=[btn.json() for btn in self.buttons], extra_classes=self.bs5_classes)
    
    def json(self):
        pass

    def __str__(self) -> str:
        return self.render()

class Page:
    def __init__(self, path: str, title: str) -> None:
        self.path = path
        self.title = title
        self.items = []
        self.html = "NO ITEMS RENDERED"

    def add(self, *items):
        for item in items:
            self.items.append(item)
        # self.items.append(items)

    def render(self):
        if len(self.items) > 0:
            self.html = "\n".join([item.render() for item in self.items])
        return self.html
    
class WebUi:
    def __init__(self) -> None:
        self.pages = []

    def add_page(self, page: Page):
        self.pages.append(page)

app = Flask(__name__)

@app.route("/")
def home():
    page = Page("/", "Abb")
    page.add(
        ButtonsGroup([
            Button("Test"),
            Button("Test"),
            Button("Test", "secondary"),
            Link("Link")
        ]),
    )
    return render_template("base.html", title=page.title, content=page.render())

if __name__ == "__main__":
    app.run(debug=True)