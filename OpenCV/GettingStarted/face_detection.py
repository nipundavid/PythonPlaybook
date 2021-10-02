import cv2

casscadePath = "Resources/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casscadePath)


imgPath = "Resources/faces.jpg"
img = cv2.imread(imgPath)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+ w, y+h), (255, 0, 0), 2)


cv2.imshow("Result", img)
cv2.waitKey(0)

