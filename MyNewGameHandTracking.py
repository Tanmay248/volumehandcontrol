import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm



pTime = 0
cTIme = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:


    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList) !=0:
        print(lmList[4])
    cTIme = time.time()
    fps = 1 / (cTIme - pTime)
    pTime = cTIme

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)