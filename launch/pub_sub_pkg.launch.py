from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pub_sub_pkg',
            executable='pub_node',
            name='publisher_node',
            output='screen'
        ),
        Node(
            package='pub_sub_pkg',
            executable='sub_node',
            name='subscriber_node',
            output='screen'
        )
    ])
