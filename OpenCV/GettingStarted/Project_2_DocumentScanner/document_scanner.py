import cv2
import numpy as np

'''
1. Capture video stream
2. Resize the video window
3. Pre-Preprocess the video 
    a) Turn in to grayscale
    b) Blur it
    c) Dilate and then Erode
4. Edge detection via canny-edge detection
5. Find the biggest contour with approximation of 4
6. Warp image
'''

widthImg = 640
heightImg = 480

cam = cv2.VideoCapture(0)
cam.set(3, widthImg)  # 3 -> code for width
cam.set(4, heightImg)  # 4 -> code for height
cam.set(10, 150)  # 10 -> code for brightness


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThreashold = cv2.erode(imgDial, kernel, iterations=1)

    return imgThreashold


def getContours(img, imgContour):
    ''' RETR_EXTERNAL-> only outer details/corners, CHAIN_APPROX_NONE-> stores absolutely all the contour points,
    https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=findcontours#findcontours '''
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = np.array([])
    maxArea = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        '''to remove noise so that only valid contours are detected'''
        if area > 5000:
            # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            '''Arc length of contours, (contours, isContourClose)'''
            perimeter = cv2.arcLength(cnt, True)
            '''Find the corners in the contours'''
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            if area > maxArea and len(approx == 4):
                print(approx)
                cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
                biggest = approx
                maxArea = area
    return biggest


def getWarp(img, biggest):
    '''The coordinates of the image that we want to warp out'''
    pts1 = np.float32(biggest)
    '''Define size of the warp image'''
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    '''Does all the heavy lifting'''
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    return imgOutput


while True:
    success, img = cam.read()
    img = cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThreshold = preProcessing(img)
    getContours(imgThreshold, imgContour)

    cv2.imshow("Web Cam", imgContour)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
