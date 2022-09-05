import cv2
import numpy as np

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        print("1")
        area= cv2.contourArea(cnt)
        print (area)
        print("1")
        #cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)

img= cv2.imread("Resources/shapes.png")
imgContour = img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)


imgBlank= np.zeros_like(img)
cv2.imshow("original", img)
cv2.imshow("gray", imgGray)
cv2.imshow("blur", imgBlur)
cv2.imshow("canny", imgCanny)
getContours(imgCanny)
cv2.imshow("blank", imgBlank)
cv2.waitKey(0);