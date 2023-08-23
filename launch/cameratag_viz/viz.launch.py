import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    composable_node = ComposableNode(name='viz', package='apriltag_viz', plugin='AprilVizNode',
                        remappings=[("image", "/sensing/camera/traffic_light/flir_camera/rectified/image_raw"),
                                    ("detections", "/sensor_kit/sensor_kit_base_link/traffic_light_left_camera/camera_link/apriltag/detection_array")
                                #     ("detections", "/apriltag/detection_array")
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
