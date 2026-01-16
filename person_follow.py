import cv2
import time
from motor_test import forward, left, right, stop, cleanup

print(">>> Person-follow robot started (HEADLESS MODE)")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

FRAME_CENTER = 160        # 320 / 2
TURN_THRESHOLD = 30

MIN_AREA = 3500
MAX_AREA = 11000

FORWARD_SPEED = 20
TURN_SPEED = 15

tracking = False
last_seen = time.time()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

tracker = None

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            stop()
            time.sleep(0.1)
            continue

        frame = cv2.resize(frame, (320, 240))

        if not tracking:
            boxes, _ = hog.detectMultiScale(
                frame,
                winStride=(8, 8),
                padding=(8, 8),
                scale=1.05
            )

            if len(boxes) > 0:
                x, y, w, h = boxes[0]
                tracker = cv2.TrackerKCF_create()
                tracker.init(frame, (x, y, w, h))
                tracking = True
                last_seen = time.time()
                print(">>> Person locked")
            else:
                stop()
 else:
            success, box = tracker.update(frame)

            if success:
                x, y, w, h = map(int, box)
                person_center = x + w // 2
                area = w * h
                error = person_center - FRAME_CENTER
                last_seen = time.time()

                if area > MAX_AREA:
                    stop()

                elif area < MIN_AREA:
                    forward(FORWARD_SPEED)

                elif error < -TURN_THRESHOLD:
                    left(TURN_SPEED)

                elif error > TURN_THRESHOLD:
                    right(TURN_SPEED)

                else:
                    stop()

            else:
                tracking = False
                stop()
                print(">>> Tracking lost")

        if time.time() - last_seen > 2.0:
            tracking = False
            stop()
            print(">>> Person lost")

        time.sleep(0.04)

except KeyboardInterrupt:
    print(">>> Stopping robot")

finally:
    stop()
    cleanup()
    cap.release()
