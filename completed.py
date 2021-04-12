import cv2
import numpy as np

cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

fcc = cv2.VideoWriter_fourcc(*'XVID')

output = cv2.VideoWriter('output.avi', fcc, 20.0, (640,480))


while True:

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, 0)
    detections = cascade_classifier.detectMultiScale(frame,scaleFactor=1.3,minNeighbors=5)

    if(len(detections) > 0):
        (x,y,w,h) = detections[0]
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    for (x,y,w,h) in detections:
     	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    # Display the resulting frame
    output.write(frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
output.release()
cv2.destroyAllWindows()