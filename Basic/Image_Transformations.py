import cv2 as cv
import numpy as np
image = cv.imread('img1.jpeg')
img = cv.resize(image,(700,1000))
#cv.imshow('img',img)

# Translation
def translate(img,x,y): #x,y stands for the number of pixels you want to shift along the x and y axis
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
#translated = translate(img,100,100)
#cv.imshow('Translated',translated)
#https://sites.google.com/view/hwangp/%E7%B7%9A%E6%80%A7%E4%BB%A3%E6%95%B8/linear-algebra/affine-transformation#h.7nkubdq9jmyc

'''# Rotation
def rotate (img,angle,rotPoint = None):
    (height,width) = img.shape[:2] #0 for height, 1 for width
    dimensions = (width,height)
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    #cv.getRotationMatrix2D(center,angle,scale)
    return cv.warpAffine(img,rotMat,dimensions)

#rotated =rotate(img,45) # counterclockwise
rotated =rotate(img,-45) # clockwise
cv.imshow('rotate',rotated)
cv.waitKey(0)'''

'''# Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)'''

#Flipping cv.flip(src,flipCode)   #flipCode(0: vertically, 1: horizontally, -1: both )
# flip = cv.flip(img,0)
# flip = cv.flip(img,1)
# flip = cv.flip(img,-1)
# cv.imshow('Flip',flip)

# Cropping
cropped = img[200:400,300:400]
cv.imshow('Flip',cropped)
cv.waitKey(0)





















