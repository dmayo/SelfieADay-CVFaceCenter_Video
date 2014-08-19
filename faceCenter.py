import time
import numpy as np
import cv2
from os import walk

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#input path
path='C:\Users\David\Dropbox\David-Christian\pictures_face'

#output path
outPath='photos'

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for fileName in f:
    if(not(len(fileName)<5 or fileName[-4:]!=".jpg")):
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
        
        if(maxFace>=0):
            face = faces[maxFace]    
            (x,y,w,h) = face
            #draw boxes
            '''
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            '''
            #resize image
            startX, startY =0,0
            centerX = x+w/2
            centerY = y+h/2
            endY, endX  = img.shape[:2]

            if(centerX>endX/2):
                startX = centerX - (endX-centerX)
            else:
                endX = centerX*2
                
            if(centerY>endY/2):
                startY = centerY - (endY-centerY)
            else:
                endY = centerY*2
            
            height = endY - startY
            width = endX - startX
            #keep aspect ratio
            if(height/720.0>width/1080.0):
                startY = centerY - (width/1080.0*720.0)/2
                endY = centerY + (width/1080.0*720.0)/2
            else:
                startX = centerX - (height/720.0*1080.0)/2
                endX = centerX + (height/720.0*1080.0)/2
            
            crop_img = img[startY:endY, startX:endX]
            img = crop_img
            
            resize_img = cv2.resize(img, (1080, 720)) 
            img = resize_img
        
    else:
        print "no face in "+fileName
        
    '''
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    '''
    #show images
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    #output images
    cv2.imwrite(outPath+"\\"+fileName,img)
    #time.sleep(3)
    cv2.destroyAllWindows()
