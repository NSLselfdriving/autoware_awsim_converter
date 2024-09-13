import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy
from autoware_control_msgs.msg import Control
from autoware_auto_control_msgs.msg import AckermannControlCommand
class ControlPublishNode(Node):
    def __init__(self):
        super().__init__('control_publish_node')
        # QoS settings
        qos_profile = QoSProfile(depth=10)
        qos_profile.durability = DurabilityPolicy.TRANSIENT_LOCAL
        # Subscribe to the /control/command/control_cmd topic
        self.subscription = self.create_subscription(
            Control,
            '/control/command/control_cmd',
            self.listener_callback,
            qos_profile
        )
        # Publisher for the /control/command/control_cmd_awsim topic
        self.publisher_ = self.create_publisher(
            AckermannControlCommand,
            '/control/command/control_cmd_awsim',
            qos_profile
        )
    def listener_callback(self, msg):
        ackermann_msg = AckermannControlCommand()
        ackermann_msg.stamp = msg.stamp
        ackermann_msg.lateral.steering_tire_angle = msg.lateral.steering_tire_angle
        ackermann_msg.lateral.steering_tire_rotation_rate = msg.lateral.steering_tire_rotation_rate
        ackermann_msg.longitudinal.speed = msg.longitudinal.velocity
        ackermann_msg.longitudinal.acceleration = msg.longitudinal.acceleration
        ackermann_msg.longitudinal.jerk = msg.longitudinal.jerk
        # Convert or copy fields from Control to AckermannControlCommand
        # Example: ackermann_msg.longitudinal.speed = msg.speed
        # Set the fields according to your specific use case
        # Publish the message to the new topic
        self.publisher_.publish(ackermann_msg)
        self.get_logger().info(f'Published control info: {ackermann_msg}')
def main(args=None):
    rclpy.init(args=args)
    node = ControlPublishNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()