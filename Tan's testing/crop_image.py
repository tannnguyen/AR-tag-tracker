import numpy as np 
import cv2

img = cv2.imread('big_image.jpg')
img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
cropped = img[175:360, 200:490]
cv2.imwrite("arrow_0.15.jpg", cropped)
cv2.imshow('img', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()