import cv2
import time

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    cv2.imshow("Camera", frame)
    time.sleep(0.1)
    if cv2.waitKey(1) == ord("q"):
        break

