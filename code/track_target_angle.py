import cv2
import numpy as np
from lib import tracker

BLUE = (255, 50, 50)
GREEN = (50, 255, 50)
RED = (50, 50, 255)
WHITE = (255, 255, 255)

def put_text(img, text, pos, color):
    return cv2.putText(img, text, pos,
                       fontFace=cv2.FONT_HERSHEY_DUPLEX,
                       fontScale=0.6, color=color)

def main():
    target = (1087, 436)
    radius = 80
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter('sample3.avi', fourcc, 6.0, (2048, 1536))
    

    while True:
        
        _, img = cap.read()

        markers = tracker.find_markers(img)
                # Track all markers on screen
        for m_id, marker in markers.items():
            cv2.drawContours(img, [marker.contour], -1, GREEN, 2)
            cv2.line(img, marker.position, marker.major_axis, WHITE, 2)
            cv2.line(img, marker.position, marker.minor_axis, WHITE, 2)
            cv2.putText(img, str(marker), marker.position,
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=0.6, color=RED)

        if 1 in markers:
            marker = markers[1]
            a = np.array(marker.major_axis)
            b = np.array(marker.position)
            target = marker.position
            c = np.array(target)
            phi = marker.angle_to_point(target)

            # If the target is close enough and we accept 
            if np.linalg.norm(c - b) < radius - np.linalg.norm(b - a):
                contour_color = GREEN
            else:
                contour_color = RED

            if abs(phi) < 10:
                deg_color = GREEN
            else:
                deg_color = RED
            cv2.drawContours(img, [marker.contour], -1, contour_color, 2)
            cv2.line(img, marker.position, target, deg_color, 2)
            cv2.line(img, marker.position, marker.major_axis, WHITE, 2)
            cv2.circle(img, target, radius, contour_color, 2)
            put_text(img, 'Angle: {0}'.format(phi), (10, 40), deg_color)
        else:
            cv2.circle(img, target, radius, RED, 2)

        # Track all markers on screen
        for m_id, marker in markers.items():
            cv2.drawContours(img, [marker.contour], -1, GREEN, 2)
            cv2.line(img, marker.position, marker.major_axis, WHITE, 2)
            cv2.line(img, marker.position, marker.minor_axis, WHITE, 2)
            cv2.putText(img, str(marker), marker.position,
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=0.6, color=RED)
        out.write(img)
        cv2.imshow('Main window', img)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    out.release()

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1944)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2592)

    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    main()

    cap.release()
    cv2.destroyAllWindows()