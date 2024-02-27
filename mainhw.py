import cv2
import os

img=cv2.imread("C:/Users/Anukriti/Desktop/all my files (anukriti)/open cv/l-1/PFP.jpg",1)
 
B, G, R = cv2.split(img)

cv2.imshow("oringnal",img)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("oringnal")

cv2.imshow("blue scale",B)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("blue scale")

cv2.imshow("red scale",R)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("red scale")

cv2.imshow("green scale",G)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("green scale")

cv2.imshow("grey scale",0)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("grey scale")

path="C:/Users/Anukriti/Desktop/all my files (anukriti)/open cv/l-1"

os.chdir(path)

cv2.imwrite("bnw.png",img)

print("saved")

cv2.waitKey(0)
cv2.destroyAllWindows()