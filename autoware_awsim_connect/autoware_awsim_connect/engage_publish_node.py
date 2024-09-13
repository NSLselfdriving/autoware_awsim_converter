import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy
from autoware_auto_vehicle_msgs.msg import Engage as AwsimEngage
from autoware_vehicle_msgs.msg import Engage

class EngagePublisher(Node):
    def __init__(self):
        super().__init__('engage_node')

        # QoS settings
        qos_profile = rclpy.qos.QoSProfile(depth=10)
        qos_profile.durability = rclpy.qos.DurabilityPolicy.TRANSIENT_LOCAL

        # Subscriber from Autoware
        self.subscription = self.create_subscription(
            Engage,
            '/vehicle/engage',
            self.listener_callback,
            qos_profile
            )
        self.subscription  # prevent unused variable warning


        # Publisher to AWSIM  
        self.publisher_ = self.create_publisher(
            AwsimEngage, 
            '/vehicle/engage_awsim', 
            qos_profile
            )

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.engage}')

        awsim_msg = Engage()
        awsim_msg.stamp = msg.stamp
        awsim_msg.engage = msg.engage

        # Publish to AWSIM
        self.publisher_.publish(awsim_msg)
        self.get_logger().info(f'Published: {awsim_msg.engage}')

def main(args=None):
    rclpy.init(args=args)
    node = EngagePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
