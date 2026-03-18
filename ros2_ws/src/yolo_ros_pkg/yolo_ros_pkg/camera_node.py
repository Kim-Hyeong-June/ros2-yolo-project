import rclpy
from rclpy.node import Node

import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class CameraNode(Node):

    def __init__(self):
        super().__init__('camera_node')

        self.publisher_ = self.create_publisher(
            Image,
            '/camera/image',
            10
        )

        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(1)

        self.timer = self.create_timer(
            0.03,
            self.timer_callback
        )

    def timer_callback(self):

        ret, frame = self.cap.read()

        if not ret:
            return

        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = CameraNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    