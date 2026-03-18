from ultralytics import YOLO
import cv2

# YOLO 모델 로드 (가벼운 모델)
model = YOLO("yolov8n.pt")

# 웹캠 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # YOLO 객체 탐지
    results = model(frame)

    # 결과 이미지 그리기
    annotated_frame = results[0].plot()

    # 화면 출력
    cv2.imshow("YOLO Webcam Detection", annotated_frame)

    # q 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
