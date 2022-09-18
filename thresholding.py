import cv2
import numpy as np

import matplotlib.pyplot as plt

img=cv2.resize(cv2.imread("logo.png",0),(512,512))
ret,THRESH_BINARY=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret1,THRESH_BINARY_INV=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret2,THRESH_TOZERO=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret3,THRESH_TOZERO_INV=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
ret4,THRESH_TRUNC=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)



images=[img,THRESH_BINARY,THRESH_BINARY_INV,THRESH_TOZERO,THRESH_TOZERO_INV,THRESH_TRUNC]
titles=["image","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TOZERO","THRESH_TOZERO_INV","THRESH_TRUNC"]


for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


plt.show()






