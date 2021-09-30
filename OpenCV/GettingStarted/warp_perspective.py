import cv2
import numpy as np

'''
To flatten out the image that is not flat
'''

img =  cv2.imread("Resources/cards.jpg")

cv2.imshow("Un-warp", img)

'''The coordinates of the image that we want to warp out'''
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])

'''Define size of the warp image'''
width, height = 250, 350
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
'''Does all the heavy lifting'''
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Warp", imgOutput)


cv2.waitKey(0)