import findFocusImage
import numpy as np
import cv2
import glob
import sys


images = findFocusImage.images
imageNames = findFocusImage.imageNames


def loadImages(pathDir):
    for file in glob.glob(pathDir):
       findFocusImage.findFocus(file)
       imageNames.append(file)

def main(argv = sys.argv):
    if len(argv) > 1:  
        path = argv[1]+'*.jpg'
        loadImages(path)
        findFocusImage.findFocus(imageNames[0],True)
    else:
        loadImages('./*.jpg')
        findFocusImage.findFocus(imageNames[0],True)

if __name__ == "__main__":  
    main()