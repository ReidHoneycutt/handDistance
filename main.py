import cv2
import pyautogui
import time
import random
from cvzone.HandTrackingModule import HandDetector
import math

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# HAND DETECTOR
detector = HandDetector(detectionCon=0.8, maxHands=1)



while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        bbox = hands[0]['bbox']
        #cv2.imshow("Image", img)
        cv2.waitKey(1)



        #time.sleep(1)
        #file.close()
        coor = str(hands[0]["lmList"][8][:-1][0])+","+str(hands[0]["lmList"][8][:-1][1])
        pyautogui.moveTo(1512-hands[0]["lmList"][8][:-1][0], hands[0]["lmList"][8][:-1][1])


