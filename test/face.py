import cv2
import dlib
import matplotlib.pyplot as plt
import numpy as np

predictor_path = 'shape_predictor_68_face_landmarks.dat'
test_img = '/home/lyb/图片/马云.jpeg'
img = cv2.imread(test_img)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

faces = detector(img, 0)
if len(faces):
    for i in range(len(faces)):
        landmarks = np.matrix([[p.x, p.y] for p in predictor(img, faces[i]).parts()])
        for point in landmarks:
            pos = (point[0, 0], point[0, 1])
            cv2.circle(img, pos, 3, color=(0, 255, 0),thickness=3)
else:
    print('Face not found!')

# opencv读取图片是BRG通道的，需要专成RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(plt.imread(test_img))
plt.axis('off')
plt.subplot(122)
plt.imshow(img)
plt.axis('off')
plt.show()