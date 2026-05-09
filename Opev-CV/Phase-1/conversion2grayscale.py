import cv2

img = cv2.imread("Phase-1\wallpaper_4k.png",1)
if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("New IMG",gray)
    cv2.waitKey(20000)
    cv2.destroyAllWindows()
else:
    print("Img not found")