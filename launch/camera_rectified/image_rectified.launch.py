import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration



def generate_launch_description():
    launch_arguments = []

    def add_launch_arg(name: str, default_value=None):
        launch_arguments.append(DeclareLaunchArgument(name, default_value=default_value))

    add_launch_arg("input_image_raw", "/sensing/camera/top/gmsl/image_raw")
    add_launch_arg("input_camera_info", "/sensing/camera/top/gmsl/camera_info")
    add_launch_arg("output_image_raw", "/sensing/camera/top/gmsl/rectified")
    add_launch_arg("output_camera_info", "/rectified/camera_info")
    # node = Node(
    #   package='output_rectified_image_py',
    #   executable='output_rectified_image_py_node',
    #   name='output_rectified_image_py_node',
    #   remappings=[
    #     ('input_image_raw', LaunchConfiguration("input_image_raw")),
    #     ('input_camera_info', LaunchConfiguration("input_camera_info")),

    #     ('output_image_raw', LaunchConfiguration("output_image_raw")),
    #     ('output_camera_info', LaunchConfiguration("output_camera_info"))],
    #   output='screen')
    
    node = Node(
      package='output_rectified_image_cpp',
      executable='output_rectified_image_cpp_node',
      name='output_rectified_image_cpp_node',
      remappings=[
        ('image_raw',  LaunchConfiguration("input_image_raw")),
        ('camera_info', LaunchConfiguration("input_camera_info")),

        ('rectified/image_raw', LaunchConfiguration("output_image_raw")),
        ('rectified/camera_info', LaunchConfiguration("output_camera_info"))],
      output='screen')
  
    return LaunchDescription(launch_arguments+[node,])
