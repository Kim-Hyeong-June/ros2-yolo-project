import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class DetectionSubscriber(Node):

    def __init__(self):
        super().__init__('detection_sub')

        self.subscription = self.create_subscription(
            String,
            '/yolo/detections',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f'Detected: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    node = DetectionSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    