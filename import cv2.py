import cv2
from ultralytics import YOLO

# Load your OpenVINO-optimized YOLO model
model = YOLO('yolov8n_openvino_model')

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for faster processing
    frame = cv2.resize(frame, (640, 640))

    # Run YOLO inference
    results = model(frame)

    # Draw bounding boxes for people (class 0)
    for r in results:
        for box, cls in zip(r.boxes.xyxy, r.boxes.cls):
            if int(cls) == 0:
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Show the video
    cv2.imshow("YOLO Live Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
