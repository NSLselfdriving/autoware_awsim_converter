import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy
from autoware_auto_vehicle_msgs.msg import TurnIndicatorsCommand as AwsimTurnIndicatorsCommand # AWSIM
from autoware_vehicle_msgs.msg import TurnIndicatorsCommand

class TurnIndicatorsCommandConverter(Node):

    def __init__(self):
        super().__init__('turn_indicators_command_converter')
        
        # QoS settings
        qos_profile = rclpy.qos.QoSProfile(depth=10)
        qos_profile.durability = rclpy.qos.DurabilityPolicy.TRANSIENT_LOCAL

        # Subscriber from Autoware
        self.subscription = self.create_subscription(
            TurnIndicatorsCommand,
            '/control/command/gear_cmd',
            self.listener_callback,
            qos_profile
            )
        
        # Publisher to AWSIM
        self.publisher = self.create_publisher(
            AwsimTurnIndicatorsommand,
            '/control/command/gear_cmd_awsim',
            qos_profile
            )
        
        self.get_logger().info('Gear Command Converter node has been started')

    def listener_callback(self, msg):

        # Convert TurnIndicatorsCommand to AwsimTurnIndicatorsCommand
        awsim_msg = AwsimTurnIndicatorsCommand()
        awsim_msg.command = msg.command
        
        # Publishe to AWSIM
        self.publisher.publish(awsim_msg)
        self.get_logger().info(f'Received and published turn_indicators command: {msg.command}')

def main(args=None):
    rclpy.init(args=args)

    turn_indicators_command_converter = TurnIndicatorsCommandConverter()

    try:
        rclpy.spin(turn_indicators_command_converter)
    except KeyboardInterrupt:
        pass
    finally:
        turn_indicators_command_converter.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
