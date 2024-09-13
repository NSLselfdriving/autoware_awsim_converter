import rclpy
from rclpy.node import Node
from autoware_auto_vehicle_msgs.msg import SteeringReport as OldSteeringReport
from autoware_vehicle_msgs.msg import SteeringReport

class SteeringStatusSubscriber(Node):
    def __init__(self):
        super().__init__('steering_status_subscriber')
        self.subscription = self.create_subscription(
            OldSteeringReport,
            '/vehicle/status/steering_status_awsim',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher to '/vehicle/status/steering_status'
        self.publisher = self.create_publisher(SteeringReport, '/vehicle/status/steering_status', 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received steering status: {msg}')

        # Convert and publish the message
        new_msg = SteeringReport()

        new_msg.stamp = msg.stamp
        new_msg.steering_tire_angle = msg.steering_tire_angle
        
        self.publisher.publish(new_msg)
        self.get_logger().info('Published message to autoware')
   

def main(args=None):
    rclpy.init(args=args)
    steering_status_subscriber = SteeringStatusSubscriber()
    rclpy.spin(steering_status_subscriber)
    steering_status_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
