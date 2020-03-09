import cv2
import sys

img=cv2.imread('./data/test.jpg')
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_model=cv2.CascadeClassifier('./env/cv2/data/haarcascade_frontalface_default.xml')
faces=face_model.detectMultiScale(gray)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    
cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()