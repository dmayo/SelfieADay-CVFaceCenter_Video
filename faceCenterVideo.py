import time
import numpy as np
import cv2
from os import walk

#input path
path='photos'
#output path
outputFile='video.avi'
#images per second
fps=20

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

height = 720
width = 1080
layers = 3

video = cv2.VideoWriter(outputFile,-1,fps,(width,height))
print len(f)
for fileName in f:
    if(not(len(fileName)<5 or fileName[-4:]!=".jpg")):
        img = cv2.imread(path+"\\"+fileName)
        #cv2.imshow('image',img)
        #cv2.waitKey(0)
        
        sizeY, sizeX  = img.shape[:2]
        if (sizeY!= height or sizeX !=width):
            img = cv2.resize(img, (1080, 720))
            
        try:
            video.write(img)
        except Exception:
            print "something went wrong"

video.release()
print "Done!"
