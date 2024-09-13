import rclpy
from rclpy.node import Node
from autoware_auto_vehicle_msgs.msg import ControlModeReport as OldControlModeReport
from autoware_vehicle_msgs.msg import ControlModeReport

class ControlModeSubscriber(Node):
    def __init__(self):
        super().__init__('control_mode_subscriber')
        self.get_logger().info('ControlModeSubscriberPublisher node has been started.')
        self.subscription = self.create_subscription(
            OldControlModeReport,
            '/vehicle/status/control_mode_awsim',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(
            ControlModeReport, 
            '/vehicle/status/control_mode',
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Current control_mode: {msg}')

        # Convert and publish the message
        new_msg = ControlModeReport()
        new_msg.stamp = msg.stamp
        new_msg.mode = msg.mode

        self.publisher.publish(new_msg)
        self.get_logger().info('Published converted control_mode report')

def main(args=None):
    rclpy.init(args=args)
    control_mode_subscriber = ControlModeSubscriber()
    rclpy.spin(control_mode_subscriber)
    control_mode_status.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
