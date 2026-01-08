# live_gui.py
from ultralytics import YOLO
import cv2

model = YOLO('/home/pi/yolov8n_openvino_model')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (640, 640))
    results = model(frame)
    for r in results:
        for box, cls in zip(r.boxes.xyxy, r.boxes.cls):
            if int(cls) == 0:
                x1,y1,x2,y2 = map(int, box)
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
    cv2.imshow('YOLO Live', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
