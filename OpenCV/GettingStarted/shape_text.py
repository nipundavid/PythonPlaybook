import cv2
import numpy as np

'''
Image with 512x512 pixels,
Has 3 channels - BRG
'''
img1 = np.zeros((512, 512,3), dtype=np.uint8)
cv2.imshow("Image", img1)

'''
: -> for whole image
[startY: destY, startX: destX] -> color that area
'''
img1[:] = 0, 255, 0
cv2.imshow("Colored Image", img1)

'''
line(image,starting_point, ending_point, color_of_line, width_of_line)
'''
cv2.line(img1, (0, 0), (256, 256), (0, 0, 255), 3)
'''
We can also get width and height from the image
But first argument is Y and Second is X
Origin(0,0) is top left corner of the image
'''
cv2.line(img1, (0, img1.shape[0]), (img1.shape[1], 0), (255, 0, 0), 3)
cv2.rectangle(img1, (0, 0), (200, 100), (0, 25, 25), thickness=2)

cv2.putText(img1, "Some text", (256, 256), cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(100, 100, 10), thickness=2)

cv2.imshow("Line On Image V2", img1)


cv2.waitKey(0)