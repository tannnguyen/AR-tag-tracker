import numpy as np
import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 


while(True):
    ret,frame = cap.read() # return a single frame in variable `frame`
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('ar_tag.jpg',frame)
        cv2.destroyAllWindows()
        break

cap.release()