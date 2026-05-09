import cv2

img = cv2.imread("wallpaper_4k.png",cv2.IMREAD_GRAYSCALE)

edgues = cv2.Canny(img , 50 , 150)

cv2.imshow("Original ", img)
cv2.imshow("canny ", edgues)
cv2.waitKey(0)
cv2.destroyAllWindows()
