import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys


images = {}

def findFocus(imagePathName):
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

    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
   
    plt.show()

    return gradientAmplValue

def showBestFocusImage(bestGradientValue):
    print('\nbest focus image ')
    findFocus(images[bestGradientValue])
    img = cv2.imread(images[bestGradientValue])
    cv2.imshow('Best Focus Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

