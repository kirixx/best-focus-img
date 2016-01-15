import cv2
import numpy as np
import sys
from msvcrt import getch
from matplotlib import pyplot as plt

import findFocusImage
import main as app

stepCounter = 0
averageGradientValue = 0
imageNames = findFocusImage.imageNames
image = findFocusImage.images

#step UP to control the stepper motor
def stepUp(event):
    step = 2
    stepNeedet = 0
    nearestImage = 0
    if event.key == 'up':
        global averageGradientValue
        if findFocusImage.getValueWithKey(averageGradientValue) == 0:
            global stepCounter
           

            '''if averageGradientValue > findFocusImage.getMinGradientValue():
                stepCounter += 1
                print(stepCounter)
                print(averageGradientValue)
                averageGradientValue -= step
            elif averageGradientValue < findFocusImage.getMaxGradientValue() and averageGradientValue > findFocusImage.getMinGradientValue():


            #elif averageGradientValue > findFocusImage.getMaxGradientValue():
               # averageGradientValue = findFocusImage.getMaxGradientValue()
                print("worst focus")
            elif averageGradientValue < findFocusImage.getMinGradientValue():
                averageGradientValue = findFocusImage.getMinGradientValue()
                print("best focus")'''
        else:
            nearestImage = findFocusImage.getDiffFromGradientValue(averageGradientValue,"UP")
            stepNeedet = nearestImage/2
            showImage(image[averageGradientValue])               
cid = plt.gcf().canvas.mpl_connect('key_press_event', stepUp)
    
#step Down to control the stepper motor
def stepDown(event):
    if event.key == 'down':
        img = cv2.imread(imageNames[1])
        plt.subplot(1,1,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        plt.show() 
cid = plt.gcf().canvas.mpl_connect('key_press_event', stepDown)
    
def main(argv = sys.argv):
    global averageGradientValue 
    if len(argv) > 1:  
        path = argv[1]+'*.jpg'
        app.loadImages(path) # load an images from directory   
        averageGradientValue = findFocusImage.getAverageGradientValue()
    else:
        app.loadImages('./*.jpg') # load an images from root
        averageGradientValue = findFocusImage.getAverageGradientValue()


#clean and set new plot
def plotConfigure():
   plt.cla()
   plt.clf()
   plt.axis("off")
   
   plt.show()

def showImage(image):
    img = cv2.imread(image) 
    plt.subplot(1,1,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show()         

if __name__ == "__main__": 
   main()
   plotConfigure()
   
