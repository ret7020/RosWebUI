from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="web_ui",
            namespace="/",
            executable="web_ui",
            name="web_ui",
            parameters=["/home/stephan/Progs/RosWeb/web_ui/launch/webui_settings.yaml"]
        ),
    ])
