"""
color space is basically a space of colors, a system of representing an array of pixel colors.
RGB is a kind of space, grayscale is color space.
*** We also have other color spaces like HSV,lamb, and many more***
"""
import cv2 as cv
import matplotlib.pyplot as plot

image = cv.imread('img1.jpeg')
img = cv.resize(image,(600,800))
# BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

'''#BGR to HSV (Hue saturation value)
"""
Hue: degree of the color
saturation: the purity of that color
value: the brightness
"""
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)'''

'''# LAB color space

Luminance - brightness/intensity of the pixel
a - how green or red is the pixel(green-red spectrum)
b - how blue or yellow is the pixel (blue-yellow spectrum)

#lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)'''

# computer read image as BGR image, but matplotlib show is RGB image
# convert BGR image to RGB image
RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plot.imshow(RGB)
plot.show()
#cv.imshow('image',img)

#cv.waitKey(0)














