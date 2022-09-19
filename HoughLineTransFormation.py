import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread(cv.samples.findFile('line.png'))
img = cv.resize(img,(1000,650))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)
lines = cv.HoughLines(edges,1,np.pi/180,200)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)


IMAGES = [img,edges]
TITLES = ["HoughLine_Image","CANN_EDGES_IMAGE "]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(IMAGES[i],cmap='gray')
    plt.title(TITLES[i])


plt.show()


#     cv.imshow("image",img)
#     cv.imshow("canny",edges)
# cv.waitKey()
# cv.destroyAllWindows()
