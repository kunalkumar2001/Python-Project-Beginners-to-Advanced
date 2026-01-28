import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot Open Webcam")
    exit()
    
print("Webcam Started")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gary, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        
    cv2.imshow("live Face Detection", frame)

    if cv2.waitKey(1) & 0xFF ==27:
        break
    
    
cap.release()
cv2.destroyAllWindows()