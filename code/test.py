import time 
import cv2
import numpy as np
from lib import tracker

BLUE = (255, 50, 50)
GREEN = (50, 255, 50)
RED = (50, 50, 255)
WHITE = (255, 255, 255)

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
while True:
    ret, img = cap.read()
    markers = tracker.find_markers(img)

    for m_id, marker in markers.items():
            cv2.drawContours(img, [marker.contour], -1, GREEN, 2)
            cv2.line(img, marker.position, marker.major_axis, WHITE, 2)
            cv2.line(img, marker.position, marker.minor_axis, WHITE, 2)
            cv2.putText(img, str(marker), marker.position,
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=0.6, color=RED)

    cv2.imshow('Main window', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''

def main():
    markers = tracker.find_markers(img)

    for m_id, marker in markers.items():
        cv2.drawContours(img, [marker.contour], -1, GREEN, 2)
        cv2.line(img, marker.position, marker.major_axis, WHITE, 2)
        cv2.line(img, marker.position, marker.minor_axis, WHITE, 2)
        cv2.putText(img, str(marker), marker.position,
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=0.6, color=RED)


if __name__ == '__main__':
    img = cv2.imread('examples/test.jpg')
    img = cv2.resize(img, None, fx=0.3, fy=0.3,
                        interpolation=cv2.INTER_LINEAR)
    main()
    cv2.imshow('Main window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''