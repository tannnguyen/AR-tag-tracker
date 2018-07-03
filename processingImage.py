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
img = cv2.imread("images.jpg", 0)

# Edge detection
ret,th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
edged=cv2.Canny(th1,127,200)

# Contours
(img2,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))

for c in cnts:
    area = cv2.contourArea(c)
    #print area
    cv2.drawContours(img,[c],0,(255,255,0),1)

cv2.imshow("contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Link: https://www.michaelpacheco.net/blog/opencv-arrow-detection