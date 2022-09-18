import cv2
import matplotlib.pyplot as plt
img=cv2.imread("batter.jpg",0)
hist=cv2.equalizeHist(img)

plt.subplot(1,2,1)
plt.title("OriginalImage")
plt.imshow(img,cmap="gray")

plt.subplot(1,2,2)
plt.title("HistEqualization")
plt.imshow(hist,cmap="gray")

plt.show()
