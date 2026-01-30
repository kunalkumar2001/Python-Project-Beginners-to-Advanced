import cv2
import numpy as np



img = cv2.imread("kunal.jpg")

img = img.astype(np.float32) / 255.0

img = cv2.pow(img, 1.2)

img[:, :, 2] = np.clip(img [:,:,2] * 1.1,0,1)
img[:, :, 1] = np.clip(img [:,:,1] * 1.05,0,1)

img = np.clip(img * 255,0, 255).astype(np.uint8)

rows, cols = img.shape[:2]
kernel_x = cv2.getGaussianKernel(cols, cols//2)
kernel_y = cv2.getGaussianKernel(rows, rows//2)
kernel = kernel_y * kernel_x.T
mask = kernel / kernel.max()

for i in range(3):
    img[:, :, i] = img[:, :, i]* mask

cv2.imwrite("modified_kunal.jpg", img)
cv2.imshow("Original", cv2.imread("kunal.jpg"))
cv2.imshow("Lo-fi Filter", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Image Saved")
