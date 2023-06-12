import cv2
import numpy as np
import dlib

#connects to your computer's default camera
cap = cv2.VideoCapture(0)

#detect the coordinates
detector = dlib.get_frontal_face_detector()

#capture frames continously
while True:

    #capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    #RGB to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    faces = detector(gray)

    #iterator to count faces

    i = 0
    for face in faces:

        #get the coordinates for faces
        x,y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x,y), (x1, y1), (0, 255, 0), 2)

        #increment iterator for each face in faces
        i = i +1

        #display the box and faces
        cv2.putText(frame, 'face num'+str(i), (x-10, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,225),2)
        print(face, i)

    #display the resulting frame
    cv2.imshow('frame', frame)

    #this command let's us quit with the "q" button on a keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#relase the capture and destroy the windows
cap.relase()
cv2.destroyAllWindows()