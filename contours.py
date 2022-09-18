import cv2

img=cv2.imread("logo.png",)
IMAGE = cv2.resize(img,(1000,500))
imggray=cv2.cvtColor(IMAGE,cv2.COLOR_BGR2GRAY)
_,th=cv2.threshold(imggray,100,199,cv2.THRESH_BINARY)



cont,hierchy=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(IMAGE,cont,-1,(0,255,0),3)



print("number of contours==",str(len(cont)))
print(cont[1])
cv2.imwrite("ContouredImage.png",IMAGE)
cv2.imshow("image",IMAGE)

cv2.waitKey()
cv2.destroyAllWindows()