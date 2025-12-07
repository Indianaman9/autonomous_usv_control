import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MotorDriver(Node):
    def __init__(self):
        super().__init__('motor_driver_node')
        
        # Listen for commands from the Brain
        self.subscription = self.create_subscription(
            String,
            'usv/motor_cmd',
            self.execute_command,
            10)
        self.subscription

    def execute_command(self, msg):
        command = msg.data
        if command == "STOP_ENGINES":
            self.get_logger().error('CRITICAL: KILLING POWER TO THRUSTERS [0 RPM]')
        elif command == "MAINTAIN_VELOCITY":
            self.get_logger().info('Engines running normally [1500 RPM]')

def main(args=None):
    rclpy.init(args=args)
    motor_driver = MotorDriver()
    rclpy.spin(motor_driver)
    motor_driver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
