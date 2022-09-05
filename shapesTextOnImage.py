import cv2
import numpy as np

img = np.zeros((512, 512,3), np.uint8)
img[0:200, 0:300]= 255,0,200 # : to specify range of colour #BGR

cv2.line(img,(0,0),(200,300),(255,255,255),3) #where,from,to,colour, thickness
cv2.rectangle(img,(0,0),(150,250),(255,255,0),2)
cv2.circle(img,(400,50),30,(0,0,255),cv2.FILLED)
cv2.putText(img,"OPEN CV", (300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1) #size, colour, thickness
cv2.imshow("image", img)
cv2.waitKey(0)