import numpy as np
import cv2


cap = cv2.VideoCapture('video.avi')
#cap = cv2.VideoCapture('green_arrow.avi')
while(True):
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([0, 80, 80])
    high_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, low_red, high_red)
    low_red = np.array([170, 80, 80])
    high_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, low_red, high_red)
    mask = mask1 | mask2
    '''
    low_green = np.array([70,50,50])
    high_green = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, low_green, high_green)
    '''
    blur = cv2.GaussianBlur(mask, (5, 5), 0)
    _, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, cnts, _ = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # loop over the contours
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)
        cX = 0
        cY = 0
        if (M["m00"] != 0):
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
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
	    #cv2.putText(frame, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (255, 255, 255), 2)
    
        # show the output image
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()