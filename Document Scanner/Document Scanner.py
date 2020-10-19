import cv2
import numpy as np

frameWidth = 980

frameHeight = 780
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    imgResult = cv2.flip(img, 1)

    cv2.imshow("Virtual Paint", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break