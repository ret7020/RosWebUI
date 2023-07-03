from .items import Page, Button, Input, Text
from std_msgs.msg import String, Int16


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
        Button(action="toggle", topic="/test_topic"),
        Text("Data: ", "rnd_string_topic", update_method="add"),
        Text(0, "rnd_int_topic", update_method="counter"),
        # Text(0, "rnd_string_topic", update_method="Counter"),
        Input("send_string_input", "number", "123", 123)
    )


    # Interacting with supervisor
    supervisor.add([String, "/pub_rnd_str"])
    supervisor.add([Int16, "/pub_rnd_int"])
    supervisor.assign_topic("rnd_string_topic", "/pub_rnd_str")
    supervisor.assign_topic("rnd_int_topic", "/pub_rnd_int")


    # Add pages
    app.add(index_page)