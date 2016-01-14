import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.widgets import Button
import sys

images = {}
imageNames = []
counter = 0
home = NavigationToolbar2.home
forward = NavigationToolbar2.forward
back = NavigationToolbar2.back

nextAx = plt.axes([0.8, 0.025, 0.1, 0.04])
nextBtn = Button(nextAx, 'Next>', color='lightgoldenrodyellow', hovercolor='0.975')
backAx = plt.axes([0.7, 0.025, 0.1, 0.04])
backBtn = Button(backAx, '<Back', color='lightgoldenrodyellow', hovercolor='0.975')
bestAx = plt.axes([0.2, 0.025, 0.12, 0.04])
bestBtn = Button(bestAx, 'Best Focus', color='lightgoldenrodyellow', hovercolor='0.975')


def newBack(event):
    global counter
    if counter != 0:
        counter -= 1
        print(counter)
        findFocus(imageNames[counter],True)    
backBtn.on_clicked(newBack) 
        
def newForward(event):
    global counter
    if counter != len(imageNames)-1:
        counter += 1
        print(counter)
        findFocus(imageNames[counter],True)   
nextBtn.on_clicked(newForward)


def findFocus(imagePathName,showPlot = False):
    img = cv2.imread(imagePathName,0)
    grd_mat = img.copy()
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    magnitude = cv2.magnitude(sobelx,sobely,grd_mat)
    gradientAmplValue = grd_mat.sum()
    print(grd_mat.max())
    print(grd_mat.min())
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

def detectBestFocusImage(event):
    minGradientAmplValue = next(iter(images.keys()))
    getAverage()
    for key in images.keys():
        if key <= minGradientAmplValue:
            minGradientAmplValue = key
            showBestFocusImage(minGradientAmplValue)           
bestBtn.on_clicked(detectBestFocusImage)

def getAverage():
    average = 0
    sum = 0
    for key in images.keys():
        sum +=key
    average = sum//len(images.keys())

    print(average)
