from flask import render_template
from typing import List
import random
import string

class ClickHandler:
    def __init__(self, action: str="none", topic: str="none", activate_message: str = "1", input_name: str = "", toggle_display: List[str]=["ON", "OFF"], toggle_values: List[str]=["1", "0"]) -> None:
        self.action = action
        self.topic = topic
        self.activate_message = activate_message
        self.input_name = input_name
        self.toggle_display = toggle_display
        self.toggle_values = toggle_values

    def html(self) -> str:
        if self.action == "event":
            return f"send_to_topic(this.id, '{self.topic}', '{self.activate_message}')"
        elif self.action == "input":
            return f"send_from_input(this.id, '{self.topic}', '{self.input_name}')"
        elif self.action == "toggle":
            return f"toggle_topic(this.id, {self.toggle_display}, {self.toggle_values}, '{self.topic}')"


class Button:
    def __init__(self, text: str="", name: str=None, type_: str="primary", action: str="none", topic: str="none", activate_message: str="1", input_name: str="", toggle_display: List[str]=["ON", "OFF"], toggle_values: List[str]=["0", "1"], style: str="", href: str="") -> None:
        self.type = type_
        self.text = text
        self.style = style
        self.name = name
        if not self.name:
            self.name = f"btn_{''.join(random.choice(string.ascii_letters) for i in range(5))}"


        # Click handler
        if action != "none" and topic != "none":
            self.click_handler = ClickHandler(action, topic, activate_message, input_name, toggle_display, toggle_values)

            if action == "toggle":
                self.text = toggle_display[0]
        else:
            self.click_handler = None
        

        # Prepare for render
        bs5_prefix = f"btn-"
        if self.style: bs5_prefix = f"{bs5_prefix}{style}-"
        self.bs5_type = f"{bs5_prefix}{self.type}"

    def render(self):
        return render_template("button.html", button=self.json())
    
    def json(self) -> dict:
        return {
            "type": self.bs5_type,
            "text": self.text,
            "click_handler": self.click_handler.html() if self.click_handler else "",
            "name": self.name
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

    def render(self) -> str:
        return render_template("button_group.html", buttons=[btn.json() for btn in self.buttons], extra_classes=self.bs5_classes)
    
    def json(self) -> dict:
        pass

    def __str__(self) -> str:
        return self.render()

class Input:
    def __init__(self, name: str, type_: str="text", placeholder: str="", start_value: str="") -> None:
        self.name = name
        self.type = type_
        self.placeholder = placeholder
        self.start_value = start_value

    def json(self) -> dict:
        return {
            "name": self.name,
            "placeholder": self.placeholder,
            "start_value": self.start_value,
            "type": self.type
        } 

    def render(self):
        return render_template("input.html", input=self.json())

class Page:
    def __init__(self, title: str, path: str = "/") -> None:
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
            content_html = "\n".join([item.render() for item in self.items])
            self.html = render_template("base.html", content=content_html)
        return self.html