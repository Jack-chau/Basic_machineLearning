# Blurring Technique
import cv2 as cv
img = cv.imread('../../Obj_Detection/img2.jpeg')

# Averaging
avarage = cv.blur(img,(7,7))
cv.imshow('avarage',avarage)

#Gauusian Blur
Gaussian = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian',Gaussian)

#Median Blur #ksize will me a 2x2 matrix
Median = cv.medianBlur(img,7)
cv.imshow('Median',Median)

#Bilateralb Blur #it apply bluring but retains the edges in the image
bilateral = cv.bilateralFilter(img,11,150,150)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)