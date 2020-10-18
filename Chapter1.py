import cv2

# import image for the project
img = cv2.imread("Resources/lenna.png")

# Display the imported image
cv2.imshow("Lenna Image", img)
cv2.waitKey(0)

# import Video
cap = cv2.VideoCapture("Resources/video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video using web cam

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break