import numpy as np
import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('tshape.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if (ret == True):
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
