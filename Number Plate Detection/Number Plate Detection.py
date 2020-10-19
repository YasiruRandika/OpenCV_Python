import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

widthImage = 480
heightImage = 640
count = 0

minArea = 500

numberPlateCascade = cv2.CascadeClassifier("../Resources/haarcascade_russian_plate_number.xml")

while True:
    success, img = cap.read()
    cv2.resize(img, (widthImage, heightImage))
    imgResult = cv2.flip(img, 1)
    imgGray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)

    numberPlates = numberPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h

        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate",(x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1, (255, 0, 255), 1)

            imgNPlate = img[y:y+h, x:x+w]
            cv2.imshow("Number Plate", imgNPlate)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("../Resources/Outputs/" + str(count) + ".jpg", imgNPlate)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 256), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)
        cv2.imshow("Result", img)
        count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# img = cv2.imread("../Resources/car.jpg")
# imgResult = img.copy()
# imgGray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
#
# numberPlates = numberPlateCascade.detectMultiScale(imgGray, 1.1, 4)
#
# for (x, y, w, h) in numberPlates:
#     area = w * h
#
#     if area > minArea:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
#         cv2.putText(img, "Number Plate",(x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1, (255, 0, 255), 1)
#
#         imgNPlate = img[y:y+h, x:x+w]
#         cv2.imshow("Number Plate", imgNPlate)
#
# cv2.imshow("Result", img)
# cv2.waitKey(0)
#
# if cv2.waitKey(1) & 0xFF == ord('s'):
#     cv2.imwrite("../Resources/Outputs" + str(count) + ".jpg", imgNPlate)
#     cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
#     cv2.putText(img, "Scan Saved", (150, 256), cv2.FONT_HERSHEY_PLAIN)
#     cv2.imshow("Result", img)
#     count += 1
