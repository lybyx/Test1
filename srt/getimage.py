
import cv2
import sys


# 读取图片
img=cv2.imread("./data/马云.jpeg")
#创建窗口

#显示图片
cv2.imshow("GetImage",img)
#窗口持续时间    "0"
cv2.waitKey(0)
#释放窗口

cv2.destroyAllWindows()
