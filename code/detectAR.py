import cv2
import numpy as np 
from ar_markers import detect_markers

cap = cv2.VideoCapture(1)

while (cap.isOpened()):
    ret, frame = cap.read()

    markers = detect_markers(frame)
    print(markers)
    for marker in markers:
        marker.highlite_marker(frame)
    
    if (ret == True):
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()