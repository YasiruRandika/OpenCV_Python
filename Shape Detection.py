import cv2
import numpy as np
img = cv2.imread("Resources/shapes.png")
img = cv2.resize(img, (640, 480))
imgContour = img.copy()

def getContours(img):
    contours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            archLength = cv2.arcLength(cnt,True)

            points = cv2.approxPolyDP(cnt, 0.02 * archLength, True)

            objectCorners = len(points)

            x, y, w, h = cv2.boundingRect(points)

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
            print(len(points))
            print(area)

            obnectType = "None"

            if objectCorners == 4:
                obnectType = "Rectangle"

                aspRation = w / float(h)
                if aspRation > 0.9 and aspRation < 1.1:
                    obnectType = "Square"
            elif objectCorners == 3:
                obnectType = "Traingle"
            elif objectCorners > 5:
                obnectType = "Circle"

            cv2.putText(imgContour, obnectType, (x + (w//2) - 10, y +(h//2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur,50, 50)
imgBlack = np.zeros_like(img)

getContours(imgCanny)
cv2.imshow("Image Contour", imgContour)

cv2.waitKey(0)

