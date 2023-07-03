import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int16
from .submodules.serve import App
from .submodules.supervisor import Supervisor
from .submodules.ui import build as ui_build
import threading
import random
import string
import time
import json
from flask_sock import Sock
import simple_websocket

class RosWebUi(Node):
    def __init__(self):
        super().__init__('webui')
        self.get_logger().info(f"{self}")
        self.app = App(self)
        self.connected_clients = []
        self.supervisor = Supervisor(self, self.send_data_to_ws_clients)
        self.sock = Sock(self.app.flask_app)
        
        @self.sock.route("/ws")
        def ws_connection_handler(sock):
            self.connected_clients.append(sock)
            while True:
                data = sock.receive() # Read data from socket
                        
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

        self.int_pub = self.create_publisher(Int16, 'pub_rnd_int', 1)
        self.timer_ = self.create_timer(0.5, self.timer_1_calback)

    def timer_callback(self):
        msg = String()
        msg.data = ''.join(random.choice(string.ascii_letters) for i in range(10))
        self.string_pub.publish(msg)

    def timer_1_calback(self):
        msg = Int16()
        msg.data = random.randint(1, 1000)
        self.int_pub.publish(msg)

    
    def listener_callback(self, data):
        self.get_logger().info(f"{data.data}")

    def send_data_to_ws_clients(self, data, topic, item_name):
        for index, client in enumerate(self.connected_clients):
            try:
                client.send(json.dumps({
                    "data": data,
                    "topic": topic,
                    "item": item_name
                }))
            except simple_websocket.ws.ConnectionClosed:
                del self.connected_clients[index] # Delete current websocket object, because client disconnected
                # self.get_logger().info("Client disconnected!")
        
def main(args=None):
    rclpy.init(args=args)
    
    webui = RosWebUi()

    rclpy.spin(webui)

    webui.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()