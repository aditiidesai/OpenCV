import cv2
import numpy as np

def empty(a):
    pass


cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,240)
cv2.createTrackbar("Hue Min", "Trackbar",0,179,empty)
cv2.createTrackbar("Hue Max", "Trackbar",37,179,empty)
cv2.createTrackbar("Sat Min", "Trackbar",35,255,empty)
cv2.createTrackbar("Sat Max", "Trackbar",255,255,empty)
cv2.createTrackbar("Val Min", "Trackbar",148,255,empty)
cv2.createTrackbar("Val Max", "Trackbar",255,255,empty)

while True:
    img = cv2.imread("Resources/car.png")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
    sat_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
    sat_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
    val_min = cv2.getTrackbarPos("Val Min", "Trackbar")
    val_max = cv2.getTrackbarPos("Val Max", "Trackbar")

    print(h_min, h_max, sat_min, sat_max, val_min, val_max)
    lower=np.array([h_min,sat_min,val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask= cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_add(img,img,mask=mask)
    cv2.imshow("original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("mask", mask)

    cv2.imshow("result", imgResult)
    cv2.waitKey(1)