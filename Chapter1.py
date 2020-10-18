import cv2

# import image for the project
img = cv2.imread("Resources/lenna.png")

# Display the imported image
cv2.imshow("Lenna Image", img)
cv2.waitKey(0)