import cv2
import numpy as np
img = cv2.imread("Resources/img.png")
print(img.shape)

imgResized = cv2.resize(img,(300,370))

imgCropped = imgResized[0:200, 200:350] #height, width

cv2.imshow("ResizedImage", imgResized)
cv2.imshow("CroppedImage", imgCropped)
cv2.waitKey(0)