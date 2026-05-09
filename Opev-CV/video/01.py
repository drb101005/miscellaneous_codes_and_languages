import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("No cam")
    cv2.imshow("yoo",frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting..")
        break

cap.release()
cv2.destroyAllWindows()