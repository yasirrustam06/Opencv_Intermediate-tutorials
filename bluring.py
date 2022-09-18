

# Python | Image blurring using OpenCV
# Image Blurring refers to making the image less clear or distinct.
# It is done with the help of various low pass filter kernels.


import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("dog.jpg")

# Applying All the Image Smoothing Or Bluring Functions

gaussian=cv2.GaussianBlur(img,(5,5),5)
median=cv2.medianBlur(img,5)
bilateral=cv2.bilateralFilter(img,9,100,78)

# DISplaying All the Three Blured Images

Images = [img,gaussian,median,bilateral]
TiTles = ["Original_Image","Gaussian_BlurImage","Median_BlurImage","Bilateral_BlurImage"]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(Images[i],cmap="gray")
    plt.title(TiTles[i])




plt.show()













