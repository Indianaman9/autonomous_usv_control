from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usv_control',
            executable='dummy_gps',
            name='gps_sensor'
        ),
        Node(
            package='usv_control',
            executable='nav_brain',
            name='autonomy_core'
        ),
        Node(
            package='usv_control',
            executable='motor_driver',
            name='propulsion_system'
        )
    ])
