from .items import Page, Button, Input
from std_msgs.msg import String


def build(app: object, supervisor: object) -> None:
    '''
    Don't change this function name
    It will call from web_ui node on ui global build(render) 
    # TODO Write a doc page in wiki about app build/render stages
    '''
    # Building simple btn's layout example
    index_page = Page("Index page", "/")
    index_page.add(
        Input("send_string_input", "text", "123", "Def value"),
        Button("Send from input above", action="input", input_name="send_string_input", topic="/test_topic"),
        Button("Send activate event to /test_topic with default value 1", action="event", topic="/test_topic"), # Send event to topic with default value = "1" (activate_message)
        Button("Changed type btn", type_="success"),
        Button("Outline style btn", style="outline"),
        Button(action="toggle", topic="/test_topic")
    )


    # Interacting with supervisor
    supervisor.add([String, "/pub_rnd_str"])





    # Add pages
    app.add(index_page)