import  cv2

img = cv2.imread("Resources/test_image.png")

imgResize = cv2.resize(img,(300,200))
'''
[startY: destY, startX: destX]
'''
imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)


cv2.waitKey(0)