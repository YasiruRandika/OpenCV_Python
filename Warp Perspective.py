import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

height = 350
width = 250

pts1 = np.float32([[239, 33], [343, 107], [135, 193], [237, 253]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Image Output", imgOutput)

cv2.waitKey(0)