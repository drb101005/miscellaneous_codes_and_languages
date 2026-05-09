import cv2

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorded = cv2.VideoWriter("New_Vid.avi", codec, 20, (frame_width, frame_height))

while True:
    success, image = cam.read()
    if not success:
        break

    recorded.write(image)
    cv2.imshow("Recording Live", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
recorded.release()
cv2.destroyAllWindows()
    