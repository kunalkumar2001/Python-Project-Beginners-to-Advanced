import cv2
import numpy as np

img = cv2.imread("kunal.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pixels = img_rgb.reshape((-1,3))
pixels = np.float32(pixels)

k=3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 100, 0.2)
_, labels, centers = cv2.kmeans(
    pixels,
    k,
    None,
    criteria,
    10,
    cv2.KMEANS_RANDOM_CENTERS   
)

centers = np.uint8(centers)
segmented = centers[labels.flatten()]
segmented = segmented.reshape(img_rgb.shape)

cv2.imshow("Segmented Image", cv2.cvtColor(segmented, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()