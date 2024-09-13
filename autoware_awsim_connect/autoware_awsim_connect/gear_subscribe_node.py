import rclpy
from rclpy.node import Node
from autoware_auto_vehicle_msgs.msg import GearReport as OldGearReport # AWSIM
from autoware_vehicle_msgs.msg import GearReport

class GearStatusSubscriber(Node):
    def __init__(self):
        super().__init__('gear_status_subscriber')
        self.subscription = self.create_subscription(
            OldGearReport,
            '/vehicle/status/gear_status_awsim',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher to '/vehicle/status/gear_status'
        self.publisher = self.create_publisher(
            GearReport, 
            '/vehicle/status/gear_status', 
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Current Gear: {msg}')

        # Convert and publish the message
        new_msg = GearReport()
        new_msg.stamp = msg.stamp
        new_msg.report = msg.report

        self.publisher.publish(new_msg)
        self.get_logger().info('Published converted gear report')
   

def main(args=None):
    rclpy.init(args=args)
    gear_status_subscriber = GearStatusSubscriber()
    rclpy.spin(gear_status_subscriber)
    gear_status_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
