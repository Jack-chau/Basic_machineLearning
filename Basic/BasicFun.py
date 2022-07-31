import cv2 as cv

def Scale (img,W_rescale,H_rescale):
    height = int(img.shape[0]*H_rescale)
    width = int(img.shape[1] * W_rescale)
    dimension = (width,height)
    return cv.resize(img,dimension,interpolation = cv.INTER_AREA)

img = cv.imread('img1.jpeg')
W_rescale = 0.3
H_rescale = 0.5
reImg = Scale(img,W_rescale,H_rescale)
'''# Convert BGR image in Gray scale
# gray = cv.cvtColor(reImg,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
# cv.waitKey(0)'''

#Blur Image cv.GauussianBlur(src,ksize,sigmaX,borderType)
blur = cv.GaussianBlur(reImg,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.imshow('Blur',blur)
cv.waitKey(0)

# Edge Cascade cv.Canny(img,threshold,threshold2)
#canny = cv.Canny(reImg,50,100)
canny = cv.Canny(blur,50,100)
#cv.imshow('canny',canny)

# Dilating the edge of the image cv.dilate(src,kernel,iterations)
dilated = cv.dilate(canny,(5,5),iterations=3)
#cv.imshow('Dilate',dilated)

# Eroding (dilating to the origin) cv.erode(src,kernal,iteration)
eroded = cv.erode(dilated,(3,3),iterations = 1)
# cv.imshow('Eroded',eroded)

#Resize cv.resize(src,dsize)
resized = cv.resize(img,(700,1000))
resized_Linear = cv.resize(img,(700,1000),interpolation=cv.INTER_LINEAR)
resized_Cubic = cv.resize(img,(700,1000),interpolation=cv.INTER_CUBIC)
# cv.imshow('resized',resized)
# cv.imshow('resized_Linear',resized_Linear)
# cv.imshow('resized_Cubic',resized_Cubic)

# Cropping #height,width
cropping = img[730:1000,570:750]
# cv.imshow('cropping',cropping)
# cv.waitKey(0)