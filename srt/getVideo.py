import cv2
import sys
sys.path.append('~/gitTest/env')
sys.path.append('~/gitTest/data')
#1.图像灰度处理，并返回灰度图像和人脸尺寸
Video=cv2.VideoCapture('./data/wuyuxin.mp4')
fps=Video.get(cv2.CAP_PROP_FPS)#
size=(int(Video.get(cv2.CAP_PROP_FRAME_WIDTH)),int(Video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fNUMS=Video.get(cv2.CAP_PROP_FRAME_COUNT)

face_model=cv2.CascadeClassifier('./env/cv2/data/haarcascade_frontalface_default.xml')
print(fps)
while True:
    ret,img=Video.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_model.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("wuyuxin",img)
    cv2.waitKey(int(fps))
Video.release()
cv2.destroyAllWindows()

# gray=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)
# face_model=cv2.CascadeClassifier('./env/cv2/data/haarcascade_frontalface_default.xml')
# faces=face_model.detectMultiScale(gray,1.1,3,0,(120,120))
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
# cv2.imshow("wuyuxin",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
