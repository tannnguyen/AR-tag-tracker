import numpy as np
import cv2

image = cv2.imread("arrow_0.25.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu = cv2.bitwise_not(otsu)
cv2.imshow('otsu', otsu)
_, cnts, _ = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]))
	cY = int((M["m01"] / M["m00"]))
	
	perimeter = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.04*perimeter, True)
	if (len(approx) == 7):
		shape = "arrow"
	else:
		shape = "undefined"
 
	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)
 
	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)
