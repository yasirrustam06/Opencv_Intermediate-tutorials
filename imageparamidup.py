import cv2
import numpy as np



img=cv2.imread("batter.jpg")
layer=img.copy()


for i in range(3):
    layer=cv2.pyrUp(layer)
    cv2.imshow(str(i),layer)

cv2.imshow("original image",img)
cv2.waitKey()
cv2.destroyAllWindows()