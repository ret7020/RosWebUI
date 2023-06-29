import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .submodules.serve import App
from .submodules.items import Page
from .submodules.ui import build as ui_build
import threading
# from web_ui.web_ui.items import Page, ButtonsGroup, Button, Link


class RosWebUi(Node):
    def __init__(self):
        super().__init__('webui')
        self.get_logger().info(f"{self}")
        self.app = App(self)
        ui_build(self.app)

        threading.Thread(target=self.app.start).start()

        # Topics sub
        # Test topics
        self.subscription = self.create_subscription(
            String,
            'test_topic',
            self.listener_callback,
        1)
    
    def listener_callback(self, data):
        self.get_logger().info(f"{data.data}")

    
        
        
def main(args=None):
    rclpy.init(args=args)

    webui = RosWebUi()

    rclpy.spin(webui)

    webui.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()