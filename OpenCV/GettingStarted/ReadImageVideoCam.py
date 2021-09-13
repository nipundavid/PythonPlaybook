import cv2

"""
Read Image and show
"""
img = cv2.imread("Resources/test_image.png")
cv2.imshow("Image", img)
cv2.waitKey(0)

"""
Read Video play
press q to quit
"""
vid = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, vidFrame = vid.read()
    if vidFrame is None:
        break
    cv2.imshow("Video", vidFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


"""
Enable web cam and show feed,
size of feed is 640x480,
press q to quit
"""
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # 3 -> code for width
cam.set(4, 480)  # 4 -> code for height
cam.set(10, 100)  # 10 -> code for brightness
while True:
    success, vidFrame = cam.read()
    cv2.imshow("Web Cam", vidFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
