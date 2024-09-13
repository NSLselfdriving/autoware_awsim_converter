import rclpy
from rclpy.node import Node
from autoware_auto_vehicle_msgs.msg import VelocityReport as OldVelocityReport
from autoware_vehicle_msgs.msg import VelocityReport

class VelocityStatusSubscriber(Node):
    def __init__(self):
        super().__init__('velocity_status_subscriber')
        self.subscription = self.create_subscription(
            OldVelocityReport,
            '/vehicle/status/velocity_status_awsim',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher to '/vehicle/status/velocity_status'
        self.publisher = self.create_publisher(VelocityReport, '/vehicle/status/velocity_status', 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Current velocity: {msg} m/s')

        # Convert and publish the message
        new_msg = VelocityReport()
        new_msg.header = msg.header
        new_msg.longitudinal_velocity = msg.longitudinal_velocity
        new_msg.lateral_velocity = msg.lateral_velocity
        new_msg.heading_rate = msg.heading_rate

        self.publisher.publish(new_msg)
        self.get_logger().info('Published converted velocity report')
   

def main(args=None):
    rclpy.init(args=args)
    velocity_status_subscriber = VelocityStatusSubscriber()
    rclpy.spin(velocity_status_subscriber)
    velocity_status_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
