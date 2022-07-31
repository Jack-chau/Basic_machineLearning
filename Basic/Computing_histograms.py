"""
Computing histograms:
    Computing histograms allows you to visualize the distribution of pixel intensities in an image.
"""
import cv2 as cv
import matplotlib.pyplot as plot
img = cv.imread('../../Obj_Detection/img2.jpeg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

'''# Grayscale histogram
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
plot.figure()
plot.title('Grayscale Histogram')
plot.xlabel('Bins')
plot.ylabel(' # of pixels')
plot.plot(gray_hist)
plot.xlim([0,256])
plot.show()'''

# Color Histograms
plot.figure()
plot.title('Grayscale Histogram')
plot.xlabel('Bins')
plot.ylabel(' # of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plot.plot(hist,color=col)
    plot.xlim([0,256])
plot.show()

cv.waitKey(0)










