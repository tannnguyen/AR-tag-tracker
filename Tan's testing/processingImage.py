import numpy as np 
import cv2 

# Alternative: Read in the arrow image and test on them. 
# Read image in grayscale
img = cv2.imread("arrow_0.15.jpg")
rows, cols, colors = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
#img = cv2.warpAffine(img,M,(cols,rows))

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low_red = np.array([0, 70, 50])
high_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, low_red, high_red)
low_red = np.array([170, 70, 50])
high_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, low_red, high_red)
mask = mask1 | mask2

# Edge detection
#threshold = cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)
blur = cv2.GaussianBlur(mask, (5, 5), 0)
_, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('otsu', otsu)
kernel = np.ones((4, 4), np.uint8)

edged=cv2.Canny(otsu,100,200)
cv2.imshow('edged', edged)
minLineLength = 5
maxLineGap = 10
dilation = cv2.dilate(edged, kernel, iterations=3)
cv2.imshow('dilation', dilation)

lines = cv2.HoughLinesP(dilation,1,np.pi/180,40, minLineLength, maxLineGap)

max_y = -1
max_y_line = []
min_y = np.inf
min_y_line = []
min_x = np.inf
min_x_line = []
max_x = -1
max_x_line = []

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        print(x1, x2, y1, y2, sep=" ")
        if (x1 > max_x):
            max_x = x1
            max_x_line = line
        if (x2 > max_x):
            max_x = x2
            max_x_line = line
        if (x1 < min_x):
            min_x = x1
            min_x_line = line
        if (x2 < min_x):
            min_x = x2
            min_x_line = line

        if (y1 > max_y):
            max_y = y1
            max_y_line = line
        if (y2 > max_y):
            max_y = y2
            max_y_line = line
        if (y1 < min_y):
            min_y = y1
            min_y_line = line
        if (y2 < min_y):
            min_y = y2
            min_y_line = line

print(max_x_line)
print(max_y_line)
print(min_x_line)
print(min_y_line)
dest = np.ones((rows, cols))
for x1,y1,x2,y2 in max_x_line:
    cv2.line(dest,(x1,y1),(x2,y2),(0,255,0),2)
for x1,y1,x2,y2 in max_y_line:
    cv2.line(dest,(x1,y1),(x2,y2),(0,255,0),2)
for x1,y1,x2,y2 in min_y_line:
    cv2.line(dest,(x1,y1),(x2,y2),(0,255,0),2)
for x1,y1,x2,y2 in min_x_line:
    cv2.line(dest,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("dist", dest)

cv2.imshow('houghlines',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Link: https://www.michaelpacheco.net/blog/opencv-arrow-detection
