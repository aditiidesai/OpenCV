import cv2
import numpy as np
print("done")

img = cv2.imread("Resources/img.png")


kernel = np.ones((5,5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray, (7,7),0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)
imgEroded = cv2.erode(imgDialation, kernel, iterations= 1)

cv2.imshow("Output", img)
cv2.imshow("Gray image", imgGray) #grey scale image
cv2.imshow("Blur image", imgBlur) #blur image
cv2.imshow("Canny", imgCanny) #edge image
cv2.imshow("Dialation image", imgDialation) #highlighting edge image
cv2.imshow("Eroded image", imgEroded)

cv2.waitKey(0)
