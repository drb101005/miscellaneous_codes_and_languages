# Tasks to do : 
#     Load an Img 
#     Convert to Gray Scale
#     Display the Img 
#     Save a copy 

import cv2

img = cv2.imread("wallpaper_4k.png",1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("New",gray)
cv2.waitKey(20000)
cv2.destroyAllWindows()

cv2.imwrite("New_Photo.jpg",gray)

