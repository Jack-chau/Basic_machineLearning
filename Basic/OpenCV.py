import cv2 as cv
import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

'''# for reading image
img = cv.imread('img1.jpeg')
cv.imshow('No_war',img)
cv.waitKey(0)'''

# Reading video
# capture = cv.VideoCapture('video1.mp4')
#
# while True:
#     isTrue, frame = capture.read() # is True is refer to whether the video is read successfully
#     cv.imshow('DSG_M4',frame)
#     key = cv.waitKey(25) #millisecinds
#     if key == 27: #Press Esc to close the video
#         break
# capture.release()
# cv.destroyAllWindows()

# SelfCamera
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read() # is True is refer to wether the video is read successfully
#     cv.imshow('Camera',frame)
#     key = cv.waitKey(25) #millisecinds
#     if key == 27: #Press Esc to close the video
#         break
# capture.release()
# cv.destroyAllWindows()
