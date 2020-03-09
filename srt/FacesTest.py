import cv2
import os
import sys
sys.path.append('~/gitTest/data')
sys.path.append('~/gitTest/env')

def getFaces(img):
    gray=cv2.cvt