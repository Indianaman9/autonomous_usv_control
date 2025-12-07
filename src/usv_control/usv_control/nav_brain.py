import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NavBrain(Node):
    def __init__(self):
        super().__init__('nav_brain_node')
        # LISTEN to the GPS
        self.subscription = self.create_subscription(
            String, 'usv/gps_data', self.listener_callback, 10)
        
        # TALK to the Motors (New Feature)
        self.command_publisher = self.create_publisher(
            String, 'usv/motor_cmd', 10)

    def listener_callback(self, msg):
        gps_string = msg.data
        cmd_msg = String()
        
        try:
            # Logic: If the 6th digit is > 5, we are drifting
            drift_value = int(gps_string.split()[1][6]) 
            
            if drift_value > 5:
                self.get_logger().warning('DRIFT DETECTED!')
                cmd_msg.data = "STOP_ENGINES"
            else:
                cmd_msg.data = "MAINTAIN_VELOCITY"
                
            # Send the order to the engine room
            self.command_publisher.publish(cmd_msg)
            self.get_logger().info(f'Sent Command: {cmd_msg.data}')

        except (ValueError, IndexError):
            pass

def main(args=None):
    rclpy.init(args=args)
    nav_brain = NavBrain()
    rclpy.spin(nav_brain)
    nav_brain.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
