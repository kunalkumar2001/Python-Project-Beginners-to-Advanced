import cv2 as cv
import datetime

qr = cv.QRCodeDetector()
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open webcam")
    exit()

scanned_data = set()

print("📷 Stylish QR Scanner | Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    # Top banner
    cv.rectangle(frame, (0, 0), (w, 60), (30, 30, 30), -1)
    cv.putText(frame, "QR Code Scanner",
               (20, 40), cv.FONT_HERSHEY_SIMPLEX,
               1, (0, 255, 255), 2)

    data, bbox, _ = qr.detectAndDecode(frame)

    if bbox is not None and data:
        bbox = bbox.astype(int)

        # Draw glowing box
        for i in range(len(bbox)):
            cv.line(frame,
                    tuple(bbox[i][0]),
                    tuple(bbox[(i + 1) % len(bbox)][0]),
                    (0, 255, 0), 3)

        # Status box
        cv.rectangle(frame, (0, h - 60), (w, h), (0, 120, 0), -1)
        cv.putText(frame, "QR Detected",
                   (20, h - 20),
                   cv.FONT_HERSHEY_SIMPLEX, 0.9,
                   (255, 255, 255), 2)

        # Show data
        cv.putText(frame, data,
                   (20, h - 90),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8,
                   (0, 255, 0), 2)

        # Save unique scans
        if data not in scanned_data:
            scanned_data.add(data)
            with open("qr_scans.txt", "a") as f:
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{time} | {data}\n")

    else:
        # Scanning mode
        cv.rectangle(frame, (0, h - 60), (w, h), (60, 60, 60), -1)
        cv.putText(frame, "Scanning...",
                   (20, h - 20),
                   cv.FONT_HERSHEY_SIMPLEX, 0.9,
                   (200, 200, 200), 2)

    cv.imshow("Attractive QR Scanner", frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
