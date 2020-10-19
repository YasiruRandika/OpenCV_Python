import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

widthImage = 480
heightImage = 640


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)

    kernel = np.ones((5, 5))
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThreshold = cv2.erode(imgDilation, kernel, iterations=1)

    return imgThreshold


def getContours(img):
    x, y, w, h = 0, 0, 0, 0
    countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    maxArea = 3000
    biggest = np.array([])

    for cnt in countours:
        area = cv2.contourArea(cnt)

        if area > 3000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            if len(approx) == 4 and area > maxArea:
                cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
                biggest = approx
                maxArea = area

    return biggest


def reOrderPoints(myPoints):
    myPoints = myPoints.reshape(4, 2)
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    difference = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(difference)]
    myPointsNew[2] = myPoints[np.argmax(difference)]

    return myPointsNew


def getWarpPerspective(img, biggest):
    biggest = reOrderPoints(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImage, 0], [0, heightImage], [widthImage, heightImage]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImage, heightImage))

    imgCropped = imgOutput[10:imgOutput.shape[1] - 10, 10: imgOutput.shape[0] - 10]
    imgCropped = cv2.resize(imgCropped, (widthImage, heightImage))

    return imgCropped


def stackImages(imgArray, scale, lables=[]):
    sizeW = imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]

    rows = len(imgArray)
    cols = len(imgArray[0])

    if isinstance(imgArray[0], list) == False:
        sizeW = imgArray[0].shape[1]
        sizeH = imgArray[0].shape[0]
        cols = 1

    if isinstance(imgArray[0], list) == False & len(imgArray) == 1:
        rows = 1
        cols = 1

    isList = isinstance(imgArray[0], list)
    print(isList)
    print(len(imgArray))

    print(str(rows) + " cols " + str(cols))

    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        print("Hello")
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        hor_con = np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth = int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range(0, cols):
                print(str(d) + " " + str(c))
                cv2.rectangle(ver, (c * eachImgWidth, eachImgHeight * d),
                              (c * eachImgWidth + len(lables[d][c]) * 13 + 27, 30 + eachImgHeight * d), (255, 255, 255),
                              cv2.FILLED)
                cv2.putText(ver, lables[d][c], (eachImgWidth * c + 10, eachImgHeight * d + 20),
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 255), 2)
    return ver



# while True:
#     success, img = cap.read()
#     cv2.resize(img, (widthImage, heightImage))
#     imgResult = cv2.flip(img, 1)
#     imgContour = imgResult.copy()
#
#     imgThreshold = preProcessing(imgResult)
#     biggest = getContours(imgThreshold)
#
#     cv2.imshow("Contour", imgContour)
#
#     if len(biggest) != 0:
#         print(biggest)
#         outputImage = getWarpPerspective(imgResult, biggest)
#         cv2.imshow("Output", outputImage)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


img = cv2.imread("../Resources/document.jpg")
cv2.resize(img, (widthImage, heightImage))

imgContour = img.copy()

imgThreshold = preProcessing(img)
biggest = getContours(imgThreshold)
print(biggest)

if len(biggest) != 0:
    cv2.imshow("Contour", imgContour)
    outputImage = getWarpPerspective(img, biggest)

    imgArray = [[img, imgContour],
                [imgThreshold, outputImage]]

    outputImage = stackImages(imgArray, 1)
    cv2.imshow("Output", outputImage)
    cv2.waitKey(0)
