import cv2 as cv
'''# Resize and rescale images and video frames
def rescaleFrame (frame,scale = 0.75): #frame is height x width
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('video1.mp4')
##### Example 2:
def changeRes (width,height):  #3 and 4 check propld
    capture.set(3,width)
    capture.set(4,height)
#https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=get#cv2.VideoCapture.set
#####
while True:
    isTrue, frame = capture.read() # is True is refer to whether the video is read successfully
    frame_resize = rescaleFrame(frame)
    cv.imshow('DSG_M4',frame)
    cv.imshow('resized_DSG_M4',frame_resize)
    key = cv.waitKey(25) #millisecinds
    if key == 27: #Press Esc to close the video
        break
capture.release()
cv.destroyAllWindows()'''
'''
# Rescale image
def rescaleFrame (frame,scale = 0.5): #frame is height x width
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)
img = cv.imread('img1.jpeg')
resized_image = rescaleFrame(img)
cv.imshow('rescaled_image',resized_image)
cv.waitKey(0)'''

