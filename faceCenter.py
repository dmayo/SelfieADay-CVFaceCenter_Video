import numpy as np
import cv2
from os import walk

path='C:\Users\David\Dropbox\David-Christian\pictures_face'

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for fileName in f:
    if(len(fileName)<5 or fileName[-4:]!=".jpg"):
        break
    img = cv2.imread(path+"\\"+fileName,1)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
