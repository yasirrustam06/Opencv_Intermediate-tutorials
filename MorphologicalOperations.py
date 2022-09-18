import matplotlib.pyplot as plt
import cv2
import numpy as np



img=cv2.imread("j.png")
kernel = np.ones((5,5),np.uint8)

dilation=cv2.dilate(img,kernel,iterations=1)

errosion=cv2.erode(img,kernel,iterations=1)

opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

#It is the difference between dilation and erosion of an image.

morph_gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)


#It is the difference between input image and Opening of the image. Below example is done for a 9x9 kernel.

top_hat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,np.ones((13,13)))


#It is the difference between the closing of the input image and input image.

Black_Hat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,np.ones((13,13)))




images=[img,dilation,errosion,opening,closing,morph_gradient,top_hat,Black_Hat]
titles=["image","dilation","errosion","opening","closing","morph_gradient","top_hat","Black_Hat"]
count=8
for i in range(count):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()



