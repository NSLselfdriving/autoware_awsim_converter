from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'autoware_awsim_connect'

    return LaunchDescription([

        # Launch gear_publish_node
        Node(
            package = package_name,  
            executable = 'gear_publish_node',
            name = 'gear_command_converter',
            output = 'screen',
        ),

        # Launch gear_subscribe_node
        Node(
            package = package_name,  
            executable = 'gear_subscribe_node',
            name = 'gear_status_subscriber',
            output = 'screen',
        ),

        # Launch control_mode_subscribe_node
        Node(
            package= package_name,  
            executable = 'control_mode_subscribe_node',
            name = 'control_mode_subscriber',
            output = 'screen',
        ),
        # Launch control_publish_node
        Node(
            package = package_name, 
            executable = 'control_publish_node',
            name = 'control_publish_node',
            output = 'screen',
        ),

        # Launch engage_publish_node
        Node(
            package = package_name, 
            executable = 'engage_publish_node',
            name = 'engage_node',
            output = 'screen',
        ),

        # Launch steering_subscribe_node
        Node(
            package = package_name, 
            executable = 'steering_subscribe_node',
            name = 'steering_status_subscriber',
            output = 'screen',
        ),

        # Launch velocity_subscribe_node
        Node(
            package = package_name, 
            executable = 'velocity_subscribe_node',
            name = 'velocity_status_subscriber',
            output = 'screen',
        ),
    ])
