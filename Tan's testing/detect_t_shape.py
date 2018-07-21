import numpy as np
import cv2

img = cv2.imread("tshape.jpg")
cv2.imshow('img', img)
cv2.waitKey(0)
img = cv2.resize(img, (0,0), fx=0.80, fy=0.80)
cropped = img[150:700, 50:500]
gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)
cv2.waitKey(0)
blur = cv2.GaussianBlur(gray, (5,5), 0)
_, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
kernel = np.ones((5,5), np.uint8)

opening = cv2.morphologyEx(otsu, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
cv2.waitKey(0)
edges = cv2.Canny(opening, 100, 200)
cv2.imshow('edges', edges)
edges_dilation = cv2.dilate(edges, kernel, iterations=5)
cv2.imshow('edges_dilation', edges_dilation)
edges_small = cv2.erode(edges_dilation, kernel, iterations=6)
cv2.imshow('edges_small', edges_small)
cv2.waitKey(0)
minLineLength = 5
maxLineGap = 10


lines = cv2.HoughLinesP(edges_small,1,np.pi/180,300, minLineLength, maxLineGap)
print(lines)
for line in lines:
    for x1,y1,x2,y2 in line:
        if (x2 == x1):
            cv2.line(cropped,(x1,y1),(x2,y2),(255,0,0),2)
        elif (y2 == y1):
            cv2.line(cropped,(x1,y1),(x2,y2),(0,0,255),2)
        else:
            angle = (y2-y1)/(x2-x1)
            cv2.line(cropped,(x1,y1),(x2,y2),(0,255,0),2)
            print(angle)
        

cv2.imshow('houghlines',cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
    