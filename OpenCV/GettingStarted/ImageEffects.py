import cv2
import numpy as np

img = cv2.imread("Resources/test_image.png")

''' 
A matrix used to perform operation which has a size of and a value of,
A matrix of 5x5 with all 1
'''
kernel = np.ones((5, 5), np.uint8)

imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
Have to be odd number -> 3,3 etc
'''
imageBlur = cv2.GaussianBlur(imageGray, (7, 7), 0)

'''
Canny Edge Detector Algo
'''
imgCanny = cv2.Canny(img, 100, 100)

'''
Trick used to increase the thickness of edges if edges not detected properly
'''
imgDialation = cv2.dilate(imgCanny, kernel, iterations =1)

'''
Opposite of dialation
'''
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imageGray)
cv2.imshow("Blur Image", imageBlur)
cv2.imshow("Canny(Edges) Image", imgCanny)
cv2.imshow("Canny(Dialation) Image", imgDialation)
cv2.imshow("Eroded(Dialation) Image", imgEroded)


cv2.waitKey(0)
