# Find an error
#
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class IntPublisher(Node):
    def __init__(self):
        # Initialize the node with the name 'pub_node'
        super().__init__('i_pub_node')
        self.i = 0
        
        # Create a publisher that publishes String messages to 'i_topic'
        self.publisher_ = self.create_publisher(Int32, 'i_topic', 10)
        
        # Timer to trigger the callback every 2.0 seconds (every other second)
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Jazzy Publisher node started. Publishing every 2 seconds.')

    def timer_callback(self):
        msg = Int32()
        self.i += 1
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = IntPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
