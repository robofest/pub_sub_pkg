from launch.actions import ExecuteProcess

from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription([
        # Launch Publisher with a custom xterm title
        ExecuteProcess(
            cmd=[
                'xterm',
                '-fa', 'Monospace',      # Sets the font family
                '-fs', '12',             # Sets the font size (increase this as needed)
                '-geometry', '80x20',   # Sets the window size (columns x rows)
                '-title', 'Publisher Node',  # <-- Adds the custom title
                '-e', 'ros2', 'run', 'pub_sub_pkg', 'i_pub_node_exe'
            ],
            output='screen'
        ),
        
        # Launch Subscriber with a custom xterm title
        ExecuteProcess(
            cmd=[
                'xterm', 
                '-fa', 'Monospace',      # Sets the font family
                '-fs', '12',             # Sets the font size (increase this as needed)
                '-geometry', '80x20',   # Sets the window size (columns x rows)
                '-title', 'Subscriber Node', # <-- Adds the custom title
                '-e', 'ros2', 'run', 'pub_sub_pkg', 'i_sub_node_exe'
            ],
            output='screen'
        )
    ])