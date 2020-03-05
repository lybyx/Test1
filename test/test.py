import  requests
import cv2
print('test')
import sys
sys.path.append('~/gitTest/data')
sys.path.append('~/gitTest/env')
img=cv2.imread('test.jpg')
cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()