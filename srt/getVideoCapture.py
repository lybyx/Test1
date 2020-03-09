import cv2
import sys
import time
sys.path.append('~/gitTest/data')
sys.path.append('~/gitTest/env')

#打开摄像头
Capture=cv2.VideoCapture(0)
cv2.namedWindow('Capture')
face_model=cv2.CascadeClassifier('./env/cv2/data/haarcascade_frontalface_default.xml')
while True:
    i=0
    i+=1
    ret, frame=Capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
   # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # faces = face_model.detectMultiScale(gray)
    faces=face_model.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
    cv2.imshow('Capture',frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    
    

Capture.release()
cv2.destroyAllWindows()