import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .submodules.serve import App
from .submodules.supervisor import Supervisor
from .submodules.ui import build as ui_build
import threading
import random
import string
import time
from flask_sock import Sock

# from web_ui.web_ui.items import Page, ButtonsGroup, Button, Link


class RosWebUi(Node):
    def __init__(self):
        super().__init__('webui')
        self.get_logger().info(f"{self}")
        self.app = App(self)
        self.connected_clients = []
        self.supervisor = Supervisor(self, self.send_data_to_ws_clients)
        self.sock = Sock(self.app.flask_app)
        
        @self.sock.route("/ws")
        def init_connection(sock):
            self.get_logger().info("Socket connected")
            self.connected_clients.append(sock)
                
        ui_build(self.app, self.supervisor)

        threading.Thread(target=self.app.start).start()

        # Topics sub
        # Test topics
        self.subscription = self.create_subscription(
            String,
            'test_topic',
            self.listener_callback,
        1)

        # Test publisher for supervisor

        self.string_pub = self.create_publisher(String, 'pub_rnd_str', 1)
        self.timer = self.create_timer(0.5, self.timer_callback)
        # while True:
        #     self.socketio.emit("sd", "Dermo")
        #     time.sleep(1)

    def timer_callback(self):
        msg = String()
        msg.data = ''.join(random.choice(string.ascii_letters) for i in range(10))
        self.string_pub.publish(msg)

    
    def listener_callback(self, data):
        self.get_logger().info(f"{data.data}")

    def send_data_to_ws_clients(self, data):
        for client in self.connected_clients:
            client.send(data)
            self.get_logger().info(f"Pending to send data: {data}")

    
        
        
def main(args=None):
    rclpy.init(args=args)

    webui = RosWebUi()

    rclpy.spin(webui)

    webui.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()