import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cam = cv2.VideoCapture(0)
cam.set(3, frameWidth)  # 3 -> code for width
cam.set(4, frameHeight)  # 4 -> code for height
cam.set(10, 150)  # 10 -> code for brightness


def findColor(img, myColors, colorValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    count = 0
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lowerb=lower, upperb=upper)
        # cv2.imshow(str(color[0]), mask)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, colorValue[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])  # 0-> color value in myColorValues
        count += 1
    return newPoints


def getContours(img):
    ''' RETR_EXTERNAL-> only outer details/corners, CHAIN_APPROX_NONE-> stores absolutely all the contour points,
    https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=findcontours#findcontours '''
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        '''to remove noise so that only valid contours are detected'''
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            '''Arc length of contours, (contours, isContourClose)'''
            perimeter = cv2.arcLength(cnt, True)
            '''Find the corners in the contours'''
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            '''Find the x, y and width and height of each bounding box'''
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

    return x + w // 2, y


def drawOnCanvas(myPoints, colorValue):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, colorValue[point[2]], cv2.FILLED)

myPoints = []  # [x, y, colorId]

while True:
    colorToDetectVal_HSV = [[133, 129, 94, 179, 255, 255]]
    # BGR
    colorToDrawBRG = [[0, 0, 255]]

    success, vidFrame = cam.read()
    imgResult = vidFrame.copy()
    newPoints = findColor(vidFrame, colorToDetectVal_HSV, colorToDrawBRG)
    if len(newPoints) != 0:
        for point in newPoints:
            myPoints.append(point)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints, colorToDrawBRG)

    cv2.imshow("Web Cam", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
