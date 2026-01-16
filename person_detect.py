import cv2

# Open default webcam
cap = cv2.VideoCapture(0)

# Initialize HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize for faster processing and consistent input size
    frame = cv2.resize(frame, (640, 480))

    # Detect people in the frame
    boxes, weights = hog.detectMultiScale(
        frame,
        winStride=(8, 8),
        padding=(16, 16),
        scale=1.05
    )

    # Draw bounding boxes around detected people
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the output frame
    cv2.imshow("Person Detect", frame)

    # Exit on ESC key press
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

