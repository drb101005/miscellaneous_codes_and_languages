import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import numpy as np
import math

# ----------------------------
# Setup
# ----------------------------

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.9, maxHands=1)

prevHandX, prevHandY = 0, 0
firstFrame = True

deadZone = 3

LEFT_THRESHOLD = 160
RIGHT_THRESHOLD = 40

leftReady = True
rightReady = True

# ----------------------------
# Main Loop
# ----------------------------

while True:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)

        handX, handY = lmList[8][0], lmList[8][1]

        # ----------------------------
        # CLUTCH MODE (Fist)
        # ----------------------------
        if fingers == [0,0,0,0,0]:
            firstFrame = True
            cv2.putText(img, "CLUTCH", (20,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0,0,255), 2)
            cv2.imshow("Gesture Mouse", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue

        # Initialize tracking
        if firstFrame:
            prevHandX, prevHandY = handX, handY
            firstFrame = False

        dx = handX - prevHandX
        dy = handY - prevHandY

        # Dead zone
        if abs(dx) < deadZone:
            dx = 0
        if abs(dy) < deadZone:
            dy = 0

        # Acceleration
        speed = math.sqrt(dx**2 + dy**2)

        if speed < 5:
            sensitivity = 1.5
        elif speed < 15:
            sensitivity = 2.5
        else:
            sensitivity = 4

        moveX = dx * sensitivity
        moveY = dy * sensitivity

        # Detect movement/scroll modes
        isMoveMode = fingers == [0,1,0,0,0]
        isScrollMode = fingers == [0,1,1,0,0]

        # ----------------------------
        # MOVE MODE
        # ----------------------------
        if isMoveMode:
            pyautogui.moveRel(moveX, moveY)
            cv2.putText(img, "MOVE", (20,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0,255,0), 2)

        # ----------------------------
        # SCROLL MODE
        # ----------------------------
        elif isScrollMode:
            pyautogui.scroll(int(-moveY))
            cv2.putText(img, "SCROLL", (20,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255,0,0), 2)

        # ----------------------------
        # THUMB + PINKY DISTANCE
        # ----------------------------
        distTP, _, _ = detector.findDistance(
            lmList[4][0:2], lmList[20][0:2], img
        )

        # LEFT CLICK (Far distance)
        if distTP > LEFT_THRESHOLD and leftReady:
            pyautogui.click()
            leftReady = False
            rightReady = True

        # RIGHT CLICK (Close distance) — DISABLED during Move/Scroll
        elif distTP < RIGHT_THRESHOLD and rightReady and not isMoveMode and not isScrollMode:
            pyautogui.rightClick()
            rightReady = False
            leftReady = True

        # Reset zone
        if 60 < distTP < 140:
            leftReady = True
            rightReady = True

        prevHandX, prevHandY = handX, handY

    else:
        firstFrame = True

    cv2.imshow("Gesture Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
