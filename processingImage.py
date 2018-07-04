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

    threshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edged=cv2.Canny(otsu,100,200)
    edged_blur = cv2.GaussianBlur(edged, (5,5), 0)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edged_blur,1,np.pi/180,100,minLineLength,maxLineGap)
    print(type(lines))
    if (type(lines) == 'numpy.ndarray'):
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)  
    cv2.waitKey(50)
  
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

'''
# Alternative: Read in the arrow image and test on them. 
# Read image in grayscale
img = cv2.imread("arrow_0.15.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Edge detection
threshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('otsu', otsu)
kernel = np.ones((4, 4), np.uint8)

edged=cv2.Canny(otsu,100,200)
cv2.imshow('edged', edged)
minLineLength = 5
maxLineGap = 10
erosion = cv2.dilate(edged, kernel, iterations=3)
cv2.imshow('erode', erosion)

lines = cv2.HoughLinesP(erosion,1,np.pi/180,40,minLineLength, maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)  
print(len(lines))       
'''
for line in lines:
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b* rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
'''
cv2.imshow('houghlines',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Link: https://www.michaelpacheco.net/blog/opencv-arrow-detection
