import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

img=cv2.imread('car.jpg')

#高斯模糊
guassian=cv2.GaussianBlur(img,(5,5),1)
#灰度图
img=cvtColor(guassian,cv2.COLOR_BGR2GRAY)
#sobel
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely=cv2.convertScaleAbs(sobely)
sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
#二值化
ret,thresh=cv2.threshold(sobelxy,127,255,cv2.THRESH_BINATY)
#闭操作
kernel=np.ones((3,3),np.uint8)
closing=cv2.morphlolgyEx(thresh,cv2.MORPH_CLOSE,kernel)
#取轮廓
binary,contours,hierarchy=cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_NOTE)
draw_img=img.copy()
res=cv2.drawContours(draw_img,contours,-1,(0,0,255),2)

