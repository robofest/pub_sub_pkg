#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StringSubscriber(Node):
    def __init__(self):
        # Initialize the node with the name 'sub_node'
        super().__init__('sub_node')
        
        # Counter to keep track of received messages
        self.counter = 0
        
        # Create a subscription to 'topic1'
        self.subscription = self.create_subscription(
            String,
            'topic1',
            self.listener_callback,
            10
        )
        self.get_logger().info('Jazzy Subscriber node started. Listening...')

    def listener_callback(self, msg):
        self.counter += 1
        self.get_logger().info(f'Received: "{msg.data}" | Counter: {self.counter}')

def main(args=None):
    rclpy.init(args=args)
    node = StringSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
