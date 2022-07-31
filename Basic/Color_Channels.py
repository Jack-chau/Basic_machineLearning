#Split and Merge Color channel
import cv2 as cv
import numpy as np

# separate a image into three color channels (shows the color in grayscale )
img = cv.imread('../../Obj_Detection/img2.jpeg')
#cv.imshow('img2',img)
b,g,r = cv.split(img)
# cv.imshow('blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

'''#Merge the picture back
merge = cv.merge([b,g,r])
cv.imshow('merge',merge)'''

# collect the color channel
blank = np.zeros(img.shape[:2],dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

cv.waitKey(5000)
cv.destroyAllWindows()
