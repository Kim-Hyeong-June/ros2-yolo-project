import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2
from ultralytics import YOLO

from std_msgs.msg import String

class YoloNode(Node):

    def __init__(self):
        super().__init__('yolo_node')

        self.subscription = self.create_subscription(
            Image,
            '/camera/image',
            self.image_callback,
            10
        )

        self.publisher_ = self.create_publisher(
            String , 
            '/yolo/detections',
            10
        )

        self.bridge = CvBridge()

        self.model = YOLO("yolov8n.pt")

    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        results = self.model(frame)

        annotated = results[0].plot()

        
        # 🔥 YOLO 결과 추출
        names = results[0].names
        boxes = results[0].boxes

        detected = []

        for box in boxes:
            cls_id = int(box.cls[0])
            detected.append(names[cls_id])

        # 🔥 String 메시지 생성
        msg_out = String()
        msg_out.data = ", ".join(detected)

        # 🔥 publish
        self.publisher_.publish(msg_out)



        cv2.imshow("YOLO Detection", annotated)
        cv2.waitKey(1)


def main(args=None):

    rclpy.init(args=args)

    node = YoloNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    