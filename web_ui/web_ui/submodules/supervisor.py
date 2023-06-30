from typing import List


class Supervisor:
    def __init__(self, node, callback, topics: List[tuple]=[]) -> None:
        '''
        Single topic struct - refer to subscribe func docs
        Stored topics struct:
        List[3] = [
            'ROS type',
            'Topic path',
            'Subscription object'
        ]
        '''
        self.node = node
        self.topics = [[*topic, self.subscribe(topic)] for topic in topics]
        self.callback = callback

    def subscription_handler(self, msg: object, topic: str):
        self.callback(msg.data)
        # self.node.get_logger().info(f"{msg.data} from {topic}")

    def subscribe(self, topic: List[tuple]):
        '''
        Topic object struct:
        List[2] = [
            'ROS type',
            'Topic path'
        ]
        '''
        return self.node.create_subscription(topic[0], topic[1], lambda msg: self.subscription_handler(msg, topic[1]), 1)


    def add(self, topic: List[tuple]) -> None:
        '''
        Add new topic to superviser
        '''
        self.topics.append([*topic, self.subscribe(topic)])
