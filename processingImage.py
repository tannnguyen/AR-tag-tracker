import numpy as np 
import cv2 

# Open camera to capture the video
'''
 cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''

# Alternative: Read in the arrow image and test on them. 
# Read image in grayscale
img = cv2.imread("images.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection
ret,th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
edged=cv2.Canny(th1,127,200)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edged,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('houghlines5.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Link: https://www.michaelpacheco.net/blog/opencv-arrow-detection