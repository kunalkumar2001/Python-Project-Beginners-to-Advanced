import cv2
import numpy as np

url = "IP Webcam Url/video"
cp = cv2.VideoCapture(url)

while True:
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Phone Camera", frame)
    q = cv2.waitKey(1)
    if q ==ord("q"):
        break
    
cv2.destroyAllWindows()
    