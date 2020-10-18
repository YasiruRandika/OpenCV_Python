from builtins import int

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# Color the whole image with Blue
img[:] = 250, 0, 0

cv2.imshow("Image", img)
cv2.waitKey(0)

# Create line on image
cv2.line(img, (0, 0), (250, 250), (255, 255, 255), 3)

cv2.imshow("Line on Image", img)
cv2.waitKey(0)

# Create line on image from stat to end
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)

cv2.imshow("Diagonal Line on Image", img)
cv2.waitKey(0)

# Rectangle on Image

cv2.rectangle(img, (300, 10), (200, 100), (232, 33, 122), 2)
cv2.imshow("Rectangle on Image", img)
cv2.waitKey(0)

# Circle on Image

# circle(image, center, radius, color, thickness)
cv2.circle(img, (420, 40), 30, (0, 33, 122), 5)
cv2.imshow("Circle on Image", img)
cv2.waitKey(0)

# Put text on Image

# circle(image, center, radius, color, thickness)
cv2.putText(img, "This is Text", (20, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (200, 200, 200), 2)
cv2.imshow("Text on Image", img)
cv2.waitKey(0)