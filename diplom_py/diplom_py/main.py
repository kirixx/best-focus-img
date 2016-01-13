import findFocusImage
import numpy as np
import cv2
import glob
import sys
from matplotlib import pyplot as plt

images = findFocusImage.images
imageNames = findFocusImage.imageNames


def loadImages(pathDir):
    for file in glob.glob(pathDir):
       findFocusImage.findFocus(file,False)
       imageNames.append(file)

if __name__ == "__main__":  
    if len(sys.argv) > 1:  
        path = sys.argv[1]+'*.jpg'
        loadImages(path)
        findFocusImage.findFocus(imageNames[0],True)
    else:
        loadImages('./*.jpg')
        findFocusImage.findFocus(imageNames[0],True)