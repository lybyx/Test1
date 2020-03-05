#opencv检测人脸测试
#2020.3.5
#功能：对导入的单幅图片检测人脸并标出

import cv2
import sys
sys.path.append('~/gitTest/env')



def detect_face(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade=cv2.CascadeClassifier('./env/cv2/data/haarcascade_frontalface_default.xml')
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)
    (x,y,w,h)=faces[0]
    return gray[y:y+2,x:x+h],faces[0]


#根据给定的（x,y)绘制矩形
def drae_rectangle(img,rect):
     (x,y,w,h)=rect
     cv2.rectangle(img,(x,y),(x+w,y+h),(128,128,0),2)


def predict(test_img):
     img=test_img.copy()
     face,rect=detect_face(img)
     drae_rectangle(img,rect)
     return img
     

image=cv2.imread('./data/马云.jpeg')
# image2=cv2.imread('./data/test.jpg')     多张人脸检测失败
predicted_img=predict(image)
# predicted_img2=predict(image2)
cv2.imshow("Face",predicted_img)
# cv2.imshow("faces",predicted_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()