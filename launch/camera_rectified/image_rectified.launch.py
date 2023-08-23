import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    node = Node(
      package='output_rectified_image',
      executable='output_rectified_image_node',
      name='output_rectified_image_node',
      remappings=[
        ('input_image_raw', '/sensing/camera/traffic_light/flir_camera/image_raw'),
        ('input_camera_info', '/sensing/camera/traffic_light/flir_camera/camera_info'),

        ('output_image_raw', '/sensing/camera/traffic_light/flir_camera/rectified/image_raw'),
        ('output_camera_info', '/sensing/camera/traffic_light/flir_camera/rectified/camera_info')],
      output='screen')
    return LaunchDescription([node])
