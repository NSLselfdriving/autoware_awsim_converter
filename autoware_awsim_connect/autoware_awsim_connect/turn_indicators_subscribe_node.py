import rclpy
from rclpy.node import Node
from autoware_auto_vehicle_msgs.msg import TurnIndicatorsReport as OldTurnIndicatorsReport
from autoware_vehicle_msgs.msg import TurnIndicatorsReport

class TurnIndicatorsStatusSubscriber(Node):
    def __init__(self):
        super().__init__('turn_indicators_status_subscriber')
        self.subscription = self.create_subscription(
            OldTurnIndicatorsReport,
            '/vehicle/status/turn_indicators_status_awsim',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher to '/vehicle/status/turn_indicators_status'
        self.publisher = self.create_publisher(TurnIndicatorsReport, '/vehicle/status/turn_indicators_status', 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Current TurnIndicators: {msg}')

        # Convert and publish the message
        new_msg = TurnIndicatorsReport()
        new_msg.stamp = msg.stamp
        new_msg.report = msg.report

        self.publisher.publish(new_msg)
        self.get_logger().info('Published converted turn_indicators report')
   

def main(args=None):
    rclpy.init(args=args)
    turn_indicators_status_subscriber = TurnIndicatorsStatusSubscriber()
    rclpy.spin(turn_indicators_status_subscriber)
    turn_indicators_status_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
