import cv2 as cv
img = cv.imread('img1.jpeg')
img = cv.resize(img,(500,800))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Person',gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
# faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

#print(f'Nmber of face found = {len(faces_rect)}')

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

#cv.imshow('Detected Face',img)
capture = cv.VideoCapture(0)
width = 1200
height =800
while True:
    isTrue, frame = capture.read()
    frame = cv.resize(frame,(width,height))
    frame = cv.flip(frame,1)

    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    mask = cv.rectangle(gray_frame,(0,500),(0,500),color=None)
    cropping = gray_frame[0:500,0:500]

    faces_rect = haar_cascade.detectMultiScale(cropping, scaleFactor=1.1, minNeighbors=9)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    # mix = cv.bitwise_or(cropping,frame)

    cv.imshow('Camera',frame)
    #
    # print(f'Number of face found = {len(faces_rect)}')

    key = cv.waitKey(27) #1s
    if key == 27: #Press Esc to close the video
        break

capture.release()