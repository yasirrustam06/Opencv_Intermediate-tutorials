import cv2
import matplotlib.pyplot as plt

Image=cv2.imread("block2.png",0)

Sobel_X=cv2.Sobel(Image,cv2.CV_64F,1,0,ksize=5)
Sobel_Y=cv2.Sobel(Image,cv2.CV_64F,0,1,ksize=5)
Sobel_XY=Sobel_X+Sobel_Y


LaplacianImage=cv2.Laplacian(Image,cv2.CV_64F)
IMAGES = [Sobel_X,Sobel_Y,Sobel_XY,LaplacianImage]
TITLES = ["SOBEL_X","SOBEL_Y","SOBEL_X+Y","LapLacIan_Image"]
count=4
for i in range(count):
    plt.subplot(2,2,i+1)
    plt.imshow(IMAGES[i],cmap='gray')
    plt.title(TITLES[i])

plt.show()
