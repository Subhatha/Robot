# person_track_sim.py
from ultralytics import YOLO
import cv2

model = YOLO('/home/pi/yolov8n_openvino_model')
cap = cv2.VideoCapture(0)

def decide(cx, w=640):
    left = 0.4*w
    right = 0.6*w
    if cx < left:
        return "turn_left"
    elif cx > right:
        return "turn_right"
    else:
        return "forward"

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (640,640))
        results = model(frame)
        acted = False
        for r in results:
            for box, cls in zip(r.boxes.xyxy, r.boxes.cls):
                if int(cls) == 0:
                    x1,y1,x2,y2 = map(int, box)
                    cx = (x1+x2)//2
                    action = decide(cx)
                    print("Person at",cx,"->",action)
                    acted = True
                    break
            if acted: break
        if not acted:
            print("No person")
except KeyboardInterrupt:
    pass
finally:
    cap.release()
