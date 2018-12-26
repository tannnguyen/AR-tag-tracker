import numpy as np
import cv2

def capturePhoto():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 

    while(True):
        ret,frame = cap.read() # return a single frame in variable `frame`
        cv2.imshow('img1',frame) #display the captured image
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
            cv2.imwrite('ar_tag.jpg',frame)
            cv2.destroyAllWindows()
            break

    cap.release()

def captureVideo():
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('test.avi', fourcc, 20.0, (640, 480))

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

