import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")
imgCards = cv2.resize(img, (276,183))
width,height= 250,350
pts1=np.float32([[24,75],[110,32],[103,182],[189,134]])
pts2= np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(imgCards, matrix, (width,height))

cv2.imshow("Image", imgCards)
cv2.imshow("BirdView Image", imgOutput)
cv2.waitKey(0)

