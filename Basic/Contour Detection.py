import cv2 as cv
import numpy as np

# Contour Detectin:
image = cv.imread('img1.jpeg')
img = cv.resize(image, (700, 900))  # width and height

# Convert image to Gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blur
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

# use canny to detect the edge
canny = cv.Canny(blur, 125, 175)

#cv.imshow('Canny Edges', canny)
# detect contour (cv.findContours(image,mode,method))
# contours is the edge in the image. return a list
# cv.RETR_LIST: RETURN all the hierarchies countours found in the image
# cv.RETR_EXTERNAL: RETURN only the outsidest hierachies
# #cv.RETR_TREE: return all the hierarchical contours, all the contours that are in a hierarchical system
# method: how to approximate the contour
# none do nothing, simple return the hierachies that make more sences
# https://blog.csdn.net/sunny2038/article/details/12889059

# can blue and canny or set thersold (binarize the image) below the lower thresh, set 0 or blank,above the upper thresh, set to white
ret, thresh = cv.threshold(gray, 100, 250,cv.THRESH_BINARY)
contoured, contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#contours, hierachies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#print(f'{len(contours)} contour(s) found!')
#cv.imshow('contoured',contoured)
## see the contour
blank = np.zeros(img.shape,dtype='uint8')
#cv.imshow('blank',blank)
# Draw the contour on the blank image

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('drawContours',blank)
cv.waitKey(5000)
