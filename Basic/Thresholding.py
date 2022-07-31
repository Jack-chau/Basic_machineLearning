import cv2 as cv

img = cv.imread('../../Obj_Detection/img2.jpeg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

'''# Simple Thresholding method
#threshold is the minimum threshold you pass in the function
#less than minimum thershold --> black
#thresh is the frame
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)'''

# Inverse Thresholding method
# less than minimum thershold --> to write
#threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)

# Adaptive Thresholding method (computer find the thersold by itself)
# less than minimum thershold --> to write
# adaptive_thersh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,
#                                        cv.THRESH_BINARY,11,3)
# Gaussian Thresholding method
adaptive_thersh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv.THRESH_BINARY,11,)

cv.imshow('thresh',adaptive_thersh)
cv.waitKey(0)
cv.destroyAllWindows()