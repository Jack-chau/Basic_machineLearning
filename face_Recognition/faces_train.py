import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek','Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# p = []
# for i in os.listdir(r'C:\Users\Jack Chau\PycharmProjects\python\python_01\OpenCV\face_Recognition'):
#     p.append(i)

DIR = r'C:\Users\Jack Chau\PycharmProjects\python\python_01\OpenCV\face_Recognition'
haar_cascade_face = cv.CascadeClassifier('haar_face.xml')

features = [] #image array of faces
labels = [] #label belong to

def create_train():
    for person in people: #path for each folder
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path): #loop every photo inside the folder
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade_face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h,x:x+w] #height and width (dimension in img)
                features.append(faces_roi)  #put the faces array detected inside a features list
                labels.append(label) #which person inside the directory

create_train()
print('Training done -----------')
# print(f'Length of the features ={len(features)}')
# print(f'Length of the labels ={len(labels)}')
features = np.array(features,dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)


