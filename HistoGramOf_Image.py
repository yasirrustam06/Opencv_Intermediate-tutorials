import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('OIP.jpg',0)

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,256])
plt.show()






