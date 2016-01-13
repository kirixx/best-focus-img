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

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')


def newBack(self, *args, **kwargs):
    global counter
    if counter != 0:
        counter -= 1
        print(counter)
        findFocus(imageNames[counter],True)    
        back(self, *args, **kwargs)
        
def newForward(self, *args, **kwargs):
    global counter
    if counter != len(imageNames)-1:
        counter += 1
        print(counter)
        findFocus(imageNames[counter],True)   
        forward(self, *args, **kwargs)

def newHome(self, *args, **kwargs):
    findFocus(imageNames[0],True)
    home(self, *args, **kwargs)

NavigationToolbar2.home = newHome
NavigationToolbar2.forward = newForward
NavigationToolbar2.back = newBack


def findFocus(imagePathName,showPlot):
    img = cv2.imread(imagePathName,0)
    grd_mat = img.copy()
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    cv2.magnitude(sobelx,sobely,grd_mat)
    gradientAmplValue = grd_mat.sum()
    images[gradientAmplValue] = imagePathName
    print(imagePathName)
    print(gradientAmplValue)
    if(showPlot == True):
        plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])   
        plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
        plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
        plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
        plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

        return plt.show()
    else:
        return gradientAmplValue
    

    




def showBestFocusImage(bestGradientValue):
    print('\nbest focus image ')
    findFocus(images[bestGradientValue])
    img = cv2.imread(images[bestGradientValue])
    cv2.imshow('Best Focus Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
button.on_clicked(showBestFocusImage)
