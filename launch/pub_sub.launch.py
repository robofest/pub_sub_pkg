from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pub_sub_pkg',
            executable='pub_node_exe',
            name='pub_node',
            output='screen'
        ),
        Node(
            package='pub_sub_pkg',
            executable='sub_node_exe',
            name='sub_node',
            output='screen'
        )
    ])
