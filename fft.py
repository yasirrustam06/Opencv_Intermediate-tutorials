import cv2 as cv
import cv2

import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('OIP.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))


plt.subplot(1,2,1)
plt.imshow(img)
plt.title("ORIginal Image")


plt.subplot(1,2,2)
plt.imshow(magnitude_spectrum,cmap='gray')
plt.title("AfterApplying_FFT")

plt.show()






