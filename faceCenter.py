import numpy as np
import cv2
from os import walk

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

path='C:\Users\David\Dropbox\David-Christian\pictures_face'

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for fileName in f:
    if(len(fileName)<5 or fileName[-4:]!=".jpg"):
        break
    img = cv2.imread(path+"\\"+fileName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, 0, (200,200))
    maxWidth = 0
    maxHeight = 0
    maxFace = -1
    
    #find biggest face
    for i in range(len(faces)):
        (x,y,w,h) = faces[i]
        if (w*h > maxWidth*maxHeight):
            maxWidth = x
            maxHeight = h
            maxFace = i
    #draw boxes
    if(maxFace>=0):
        face = faces[maxFace]    
        (x,y,w,h) = face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    else:
        print "no face in "+fileName
        
    '''
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    '''
    #show images
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

