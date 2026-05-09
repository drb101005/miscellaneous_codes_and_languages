import cv2

img = cv2.imread("Phase-1\wallpaper_4k.png",1)

if img is not None:
    cv2.imshow("Image Showing",img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
else:
    print("Img is not loaded")