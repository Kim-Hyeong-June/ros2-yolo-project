# 🚀 ROS2 YOLO Real-Time Object Detection System

## 📌 Overview

This project implements a **real-time object detection system** using **ROS2 + YOLOv8 + OpenCV**.

It captures images from a webcam, processes them through a YOLO model, and distributes detection results across ROS topics.

---

## 🛠 Tech Stack

* ROS2 (Humble)
* Python 3.10
* OpenCV
* YOLOv8 (Ultralytics)
* cv_bridge

---

## 🔄 System Architecture

```
Webcam
   ↓
Camera Node
   ↓
/camera/image (ROS Topic)
   ↓
YOLO Node
   ↓
/yolo/detections (ROS Topic)
   ↓
Detection Subscriber
```

---

## 📦 Project Structure

```
ros2-yolo-project
└── ros2_ws
    └── src
        └── yolo_ros_pkg
            ├── camera_node.py
            ├── yolo_node.py
            ├── detection_sub.py
            └── launch
                └── yolo.launch.py
```

---

## ⚙️ Features

* 📷 Real-time webcam streaming (OpenCV)
* 🧠 YOLOv8 object detection
* 🔁 ROS2 topic-based communication
* 🧩 Modular node architecture
* 🖥 Detection visualization using OpenCV
* 📡 Detection results published as ROS messages

---

## 🧠 Core Logic

### 1️⃣ Camera Node

* Captures frames using OpenCV
* Publishes images to `/camera/image`

### 2️⃣ YOLO Node

* Subscribes to `/camera/image`
* Runs YOLO inference
* Publishes detected object labels to `/yolo/detections`
* Displays annotated frames

### 3️⃣ Detection Subscriber

* Subscribes to `/yolo/detections`
* Prints detected objects in real-time

---

## ▶️ How to Run

### 1️⃣ Build workspace

```
cd ~/ros2-yolo-project/ros2_ws
colcon build
```

### 2️⃣ Source environment

```
source install/setup.bash
```

### 3️⃣ Run system

```
ros2 launch yolo_ros_pkg yolo.launch.py
```

---

## 📊 Example Output

```
Detected: person, backpack
Detected: tv
Detected: book, book
```

---

## ⚠️ Notes

* Ensure correct camera index (`cv2.VideoCapture(0 or 1)`)
* NumPy version should be < 2 for ROS compatibility
* YOLO weights (`yolov8n.pt`) will be downloaded automatically

---

## 🚀 Future Work

* Object tracking integration
* ROS2 + robot control (cmd_vel)
* RViz visualization
* Detection message standardization (vision_msgs)

---

## 💡 Key Takeaway

This project demonstrates:

✔ Integration of AI (YOLO) with ROS2
✔ Real-time image processing pipeline
✔ Publisher-Subscriber communication
✔ Modular robotic vision architecture

---

## 👨‍💻 Author

Kim Hyeongjune
