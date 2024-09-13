import rclpy
from rclpy.node import Node
from autoware_auto_vehicle_msgs.msg import HazardLightsReport as OldHazardLightsReport
from autoware_vehicle_msgs.msg import HazardLightsReport

class HazardLightsStatusSubscriber(Node):
    def __init__(self):
        super().__init__('hazard_lights_status_subscriber')
        self.subscription = self.create_subscription(
            OldHazardLightsReport,
            '/vehicle/status/hazard_lights_status_awsim',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher to '/vehicle/status/hazard_lights_status'
        self.publisher = self.create_publisher(HazardLightsReport, '/vehicle/status/hazard_lights_status', 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Current HazardLights: {msg}')

        # Convert and publish the message
        new_msg = HazardLightsReport()
        new_msg.stamp = msg.stamp
        new_msg.report = msg.report

        self.publisher.publish(new_msg)
        self.get_logger().info('Published converted hazard_lights report')
   

def main(args=None):
    rclpy.init(args=args)
    hazard_lights_status_subscriber = HazardLightsStatusSubscriber()
    rclpy.spin(hazard_lights_status_subscriber)
    hazard_lights_status_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
