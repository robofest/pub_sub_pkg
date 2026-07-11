from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Launch Publisher in a separate xterm window
        ExecuteProcess(
            cmd=[
                'xterm', '-e', 
                'ros2', 'run', 'pub_sub_pkg', 'pub_node'
            ],
            output='screen'
        ),
        
        # Launch Subscriber in another separate xterm window
        ExecuteProcess(
            cmd=[
                'xterm', '-e', 
                'ros2', 'run', 'pub_sub_pkg', 'sub_node'
            ],
            output='screen'
        )
    ])
