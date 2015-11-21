import findFocusImage
import numpy as np
import cv2
import glob
import sys
images = findFocusImage.images

def loadImages(pathDir):
    for file in glob.glob(pathDir):
        min = findFocusImage.findFocus(file)
        
    for key in images.keys():
        if key <= min:
            min = key
    findFocusImage.showBestFocusImage(min)

if __name__ == "__main__":  
    if len(sys.argv) > 1:  
        path = sys.argv[1]+'*.jpg'
        loadImages(path)
    else:
       loadImages('./*.jpg')
