#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StringPublisher(Node):
    def __init__(self):
        # Initialize the node with the name 'pub_node'
        super().__init__('pub_node')
        
        # Create a publisher that publishes String messages to 'topic1'
        self.publisher_ = self.create_publisher(String, 'topic1', 10)
        
        # Timer to trigger the callback every 2.0 seconds (every other second)
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Jazzy Publisher node started. Publishing every 2 seconds.')

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello from ROS 2 Jazzy!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
