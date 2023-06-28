import rclpy
from rclpy.node import Node
from web_ui.web_ui.serve import App
# from web_ui.web_ui.items import Page, ButtonsGroup, Button, Link


class RosWebUi(Node):
    def __init__(self):
        super().__init__('webui')
        self.app = App()


        # Topics sub
        # Add page
        
        



def main(args=None):
    rclpy.init(args=args)

    webui = RosWebUi()

    rclpy.spin(webui)

    webui.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()