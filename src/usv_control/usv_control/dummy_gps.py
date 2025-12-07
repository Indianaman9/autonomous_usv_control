import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped

class DummyGPS(Node):
    def __init__(self):
        super().__init__('dummy_gps_node')
        
        # 1. Logic Publisher (Strings for the Brain)
        self.logic_pub = self.create_publisher(String, 'usv/gps_data', 10)
        
        # 2. Visual Publisher (Points for RViz)
        self.vis_pub = self.create_publisher(PointStamped, 'usv/vis_point', 10)
        
        timer_period = 0.1  # Faster update rate for smoother circle
        # THIS IS THE FIXED LINE BELOW:
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        # --- Logic Data ---
        msg_str = String()
        msg_str.data = f'System Active: {self.i}'
        self.logic_pub.publish(msg_str)

        # --- Visual Data (Circular Motion) ---
        point_msg = PointStamped()
        point_msg.header.frame_id = "map" 
        point_msg.header.stamp = self.get_clock().now().to_msg()
        
        # MATH: Create a circle with radius 5 meters
        t = float(self.i) * 0.1
        
        point_msg.point.x = 5.0 * math.cos(t)
        point_msg.point.y = 5.0 * math.sin(t)
        point_msg.point.z = 0.0
        
        self.vis_pub.publish(point_msg)
        
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    dummy_gps = DummyGPS()
    rclpy.spin(dummy_gps)
    dummy_gps.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
