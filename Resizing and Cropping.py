import cv2

# Resizing and Cropoing

img = cv2.imread("Resources/lenna.png")

print(img.shape)
# Output will be (height, width, no_for_channel(BGR))

# Image resize - > (width, height)
img = cv2.resize(img, (400, 320))

cv2.imshow("Image", img)
cv2.waitKey(0)


# Cropping the image
imgCropped = img[0:255, 0:255]

cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)

