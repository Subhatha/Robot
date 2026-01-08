# live_headless.py
from ultralytics import YOLO
import cv2

model = YOLO('/home/pi/yolov8n_openvino_model')  # use the exported folder
cap = cv2.VideoCapture(0)  # device 0

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break
        frame = cv2.resize(frame, (640, 640))
        results = model(frame)
        found = False
        for r in results:
            for cls in r.boxes.cls:
                if int(cls) == 0:
                    print("Person detected")
                    found = True
                    break
            if found: break
except KeyboardInterrupt:
    pass
finally:
    cap.release()
