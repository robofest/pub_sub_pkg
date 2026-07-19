from launch.actions import ExecuteProcess

from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription([
        # Launch Publisher with a custom xterm title
        ExecuteProcess(
            cmd=[
                'xterm', 
                '-title', 'Publisher Node',  # <-- Adds the custom title
                '-e', 'ros2', 'run', 'pub_sub_pkg', 'pub_node_exe'
            ],
            output='screen'
        ),
        
        # Launch Subscriber with a custom xterm title
        ExecuteProcess(
            cmd=[
                'xterm', 
                '-title', 'Subscriber Node', # <-- Adds the custom title
                '-e', 'ros2', 'run', 'pub_sub_pkg', 'sub_node_exe'
            ],
            output='screen'
        )
    ])