from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    camera_node = Node(
        package='yolo_ros_pkg',
        executable='camera_node',
        name='camera_node',
        output='screen'
    )

    yolo_node = Node(
        package='yolo_ros_pkg',
        executable='yolo_node',
        name='yolo_node',
        output='screen'
    )

    detection_sub = Node(
        package = 'yolo_ros_pkg',
        executable = 'detection_sub',
        name = 'detection_sub',
        output = 'screen'
    )

    return LaunchDescription([
        camera_node,
        yolo_node,
        detection_sub
    ])
    