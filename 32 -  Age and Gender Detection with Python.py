import cv2
from deepface import DeepFace


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open webcam")
    exit()

print("📷 Webcam started | Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
    
        results = DeepFace.analyze(
            frame,
            actions=["age", "gender", "emotion"],
            enforce_detection=False
        )

        
        if isinstance(results, list):
            results = results[0]

        age = results["age"]
        gender = results["dominant_gender"]
        emotion = results["dominant_emotion"]

        label = f"{gender}, {age}, {emotion}"

        
        cv2.putText(
            frame,
            label,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

    except Exception:
        pass  

    cv2.imshow("Live Age, Gender & Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
