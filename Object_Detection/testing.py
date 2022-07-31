import cv2 as cv
img = cv.imread('img2.jpeg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray,(5,5),3)
sobelx = cv.Sobel(img,cv.CV_64F,1,0)
sobely = cv.Sobel(img,cv.CV_64F,0,1)
mix = cv.bitwise_or(sobelx,sobely)

cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('mix',mix)

cv.waitKey(0)