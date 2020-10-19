import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

widthImage = 480
heightImage = 640

while True:
    success, img = cap.read()
    cv2.resize(img, (widthImage, heightImage))
    imgResult = cv2.flip(img, 1)
    imgContour = imgResult.copy()

    cv2.imshow("Contour", imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break