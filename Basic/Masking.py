
# focus on certain parts of the image that we like to focus on
import cv2 as cv
import numpy as np
img = cv.imread('../../Obj_Detection/img2.jpeg')
blank = np.zeros(img.shape[:2],dtype='uint8')
#cv.imshow('blank',blank)

# draw a circle mask on the frame
#width and height
# mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow('masked',masked)

# Rectangle mask
mask = cv.rectangle(blank,(0,0),(500,500),color=None)
cv.imshow('mask',mask)



cv.waitKey(0)