import time
import numpy as np
import cv2
from os import walk

#input path
path='photos'
#output path
outputFile='video.avi'
#images per second
fps=5

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

height = 720
width = 1080
layers = 3

video = cv2.VideoWriter(outputFile,-1,fps,(width,height))

for fileName in f:
    img = cv2.imread(path+"\\"+fileName)
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    video.write(img)

video.release()
print "Done!"
