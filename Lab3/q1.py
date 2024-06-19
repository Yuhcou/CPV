import cv2
import numpy as np

img = cv2.imread('egg.png', 1)
img = np.array(img)
img[:,:,1] = 0
img[:,:,2] = 0
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th, res = cv2.threshold(img, 160, None, cv2.THRESH_TOZERO)
th2, res2 = cv2.threshold(img, 100, None, cv2.THRESH_TOZERO)


pic = res-res2
cv2.imshow('i', img)
cv2.waitKey()

# blur = cv2.GaussianBlur(pic, (9,9), 0)
#
# canny = cv2.Canny(blur, 30, 150, 3)
#
# dilated = cv2.dilate(canny, (1,1), iterations = 2)
#
# (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(pic, cnt, -1, (0,255,0), 2)
#
# cv2.imshow('i', dilated)
# cv2.waitKey()




#inflation, erosion
#mean shift