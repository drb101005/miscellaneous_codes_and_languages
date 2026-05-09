import cv2

img = cv2.imread("Phase-1\wallpaper_4k.png",1)
if img is not None:
    h,w,c =img.shape
    print(h,w,c)
else:
    print("Img not loaded")