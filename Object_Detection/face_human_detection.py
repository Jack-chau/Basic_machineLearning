import cv2 as cv
capture = cv.VideoCapture(0)
haar_cascade_face = cv.CascadeClassifier('haar_face.xml')
haar_upperBodies = cv.CascadeClassifier('haar_human.xml')
while True:
    isTrue, frame = capture.read()
    frame = cv.resize(frame,(1000,800))
    frame = cv.flip(frame,1)
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#Detect face
    #set mask
    mask = cv.rectangle(frame,(0,0),(400,400),color=(0,0,0),thickness=1)
    crop = gray_frame[0:400,0:400]
    faces_rect = haar_cascade_face.detectMultiScale(crop, scaleFactor=1.1, minNeighbors=1)
    #return upper coordinate,object width and height
    print(f'number of faces: {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=1)
# Human Detection (full screen)
    human_rect = haar_upperBodies.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3)
    print(f'number of humans: {len(human_rect)}')
    for (x,y,w,h) in human_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=3)

    key = cv.waitKey(27)
    if key == 27: #press esc to break
        break
    cv.imshow('Camera',frame)
capture.release()