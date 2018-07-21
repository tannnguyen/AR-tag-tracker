import numpy as np 
import cv2

# Open camera to capture the video
cap = cv2.VideoCapture('video.avi')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([0, 70, 50])
    high_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, low_red, high_red)
    low_red = np.array([170, 70, 50])
    high_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, low_red, high_red)
    mask = mask1 | mask2

    # Edge detection
    blur = cv2.GaussianBlur(mask, (5, 5), 0)
    _, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('otsu', otsu)
    kernel = np.ones((4, 4), np.uint8)
    edged=cv2.Canny(otsu,100,200)
    cv2.imshow('edged', edged)
    minLineLength = 5
    maxLineGap = 10
    erosion = cv2.dilate(edged, kernel, iterations=2)
    cv2.imshow('erode', erosion)
    cv2.waitKey(20)

    lines = cv2.HoughLinesP(erosion,1,np.pi/180,40,minLineLength, maxLineGap)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)  

    cv2.imshow('mask', mask1)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()