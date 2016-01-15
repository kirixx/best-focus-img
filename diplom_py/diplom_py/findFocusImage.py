import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
import collections

images = {}
imageNames = []
counter = 0

def back(event):
    if event.key == 'left':
        global counter
        if counter != 0:
            counter -= 1
            print(counter)
            findFocus(imageNames[counter],True)  
cid = plt.gcf().canvas.mpl_connect('key_press_event', back) 
 

        
def forward(event):
    if event.key == 'right':
        global counter
        if counter != len(imageNames)-1:
            counter += 1
            print(counter)
            findFocus(imageNames[counter],True)   
cid = plt.gcf().canvas.mpl_connect('key_press_event', forward)


def detectBestFocusImage(event):
    if event.key == 'enter':
        showBestFocusImage(getMinGradientValue())           
cid = plt.gcf().canvas.mpl_connect('key_press_event', detectBestFocusImage)

def findFocus(imagePathName,showPlot = False):
    img = cv2.imread(imagePathName,0)
    grd_mat = img.copy()
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    magnitude = cv2.magnitude(sobelx,sobely,grd_mat)
    gradientAmplValue = grd_mat.sum()//10000
    images[gradientAmplValue] = imagePathName
    print(imagePathName)
    print(gradientAmplValue)
    if(showPlot == True):
        plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])   
        plt.subplot(2,2,2),plt.imshow(magnitude,cmap = 'gray')
        plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
        plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
        plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
        
        return plt.show()
    

def showBestFocusImage(bestGradientValue):
    print('\nbest focus image ')
    img = cv2.imread(images[bestGradientValue])
    cv2.imshow('Best Focus Image',img)
    findFocus(images[bestGradientValue],True)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def getAverageGradientValue():
    average = 0
    sum = 0
    for key in images.keys():
        sum +=key
    average = sum//len(images.keys())
    return average

def getValueWithKey(key):
    for k in images.keys():
        if k == key:
            return images[key]
        else:
            return 0

def getMaxGradientValue():
    maxGradientAmplValue = next(iter(images.keys()))
    for key in images.keys():
         if key >= maxGradientAmplValue:
             maxGradientAmplValue = key
    return maxGradientAmplValue

def getMinGradientValue():
    minGradientAmplValue = next(iter(images.keys()))
    for key in images.keys():
         if key <= minGradientAmplValue:
             minGradientAmplValue = key
    return minGradientAmplValue

def getDiffFromGradientValue(key,step):
    diff = key
    minDiff = key
    sortDict = collections.OrderedDict(sorted(images.items()))
    for k in sortDict.keys():
        if k < key and step == 'UP':
            diff = key - k
        elif k > key and step == 'DOWN':
            diff = k - key
        if diff <= minDiff:
            minDiff = diff
    return minDiff




