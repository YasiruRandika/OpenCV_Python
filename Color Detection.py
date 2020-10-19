import cv2
import numpy as np

def empty():
    pass

# New Window for TrackBars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 480)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")

    print(h_min, h_max, s_max, s_min, v_min, v_max)

    lower = np.array([h_min, s_min, v_max])
    upper = np.array([h_max, s_max, v_max ])
    mask = cv2.inRange(imgHSV, lower, upper)

    img = cv2.resize(img, (400, 320))
    imgHSV = cv2.resize(imgHSV, (400, 320))
    cv2.imshow("HSV Image", imgHSV)
    mask = cv2.resize(mask, (400, 320))
    cv2.imshow("Mask", mask)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Image Result",imgResult)

    cv2.waitKey(1)