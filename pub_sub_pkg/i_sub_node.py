#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class IntSubscriber(Node):
    def __init__(self):
        # Initialize the node with the name 'sub_node'
        super().__init__('i_sub_node')
        
        # Create a subscription to 'i_topic'
        self.subscription = self.create_subscription(
            Int32,
                    ,   # <==== Complete this line
            self.listener_callback,
            10
        )
        self.get_logger().info('Jazzy Subscriber node started. Listening...')

    def                     (self, msg): # <===== Complete this line
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = IntSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
