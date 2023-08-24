import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    def add_launch_arg(name: str, default_value=None):
        launch_arguments.append(DeclareLaunchArgument(name, default_value=default_value))

    add_launch_arg("image_topic", "/sensing/camera/traffic_light/flir_camera/image_raw")
    add_launch_arg("detections", "/sensor_kit/sensor_kit_base_link/traffic_light_left_camera/camera_link/apriltag/detection_array")

    composable_node = ComposableNode(name='viz', package='apriltag_viz', plugin='AprilVizNode',
                        remappings=[("image", LaunchConfiguration("image_topic")),
                                    ("detections", LaunchConfiguration("detections"))
                                    ],)
    container = ComposableNodeContainer(
            name='viz_container',
            namespace='apriltag',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[composable_node],
            remappings=[("/apriltag/image", "/sensing/camera/traffic_light/flir_camera/image_raw/decompressed")],
            output='screen'
    )

    return launch.LaunchDescription([container])
