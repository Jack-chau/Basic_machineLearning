import cv2 as cv
import numpy as np
#cerate a 3 dimensions array for the height, width and the number of color channel
blank = np.zeros((500,500,3),dtype='uint8') #create  an blank img, dtype is unsigned int8
# cv.imshow('blank',blank)

'''# 1. Paint the image a certain color
# select all set to green (RGB):
blank[:] = 0,255,0
cv.imshow('Green',blank)
blank[:] = 0,0,255
cv.imshow('red',blank)
blank[:] = 255,0,0
cv.imshow('blue',blank)'''

'''# 2. Set differnet color in a portion
blank[400:500,200:300] = 0,0,255 # height,width
cv.imshow('blank',blank)'''

# 3. Draw a Retangle
# #cv.rectangle(img,point1,point2,color) upper-left and lower-right
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2) #thickness of the borders
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED) #thickness of the borders
# cv.rectangle(blank,(0,0),(int(blank.shape[0]/2),int(blank.shape[1]/2)),(0,255,0),thickness=cv.FILLED) # point2 = to the midpoint of the image
cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,0),thickness=cv.FILLED) #thickness of the borders
cv.imshow('Retangle',blank)
# / --> float division
# // --> integer division (math.floor)

# 4. Draw a circle cv.circle(ing,center,radius,color)
# cv.circle(blank,(255,255),(40),(0,0,255),thickness = 3)
# cv.circle(blank,(255,255),(40),(0,0,255),thickness = cv.FILLED)
# cv.imshow('circle',blank)

#5 Draw a line cv.line(img,pt1,pt2,color) #line cannot be filled
# cv.line(blank,(0,0),(255,255),(255,255,0),thickness=1)
# cv.imshow('Line',blank)

#6. Write text on image cv.putText(img,text,org,fontFace,fontScale,color,thickness) ori=origin
# cv.putText(blank,'Hello World',(150,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=1)
# cv.putText(blank,'Hello World',(150,255),cv.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255),thickness=1)
# cv.imshow('Text',blank)


cv.waitKey(0)