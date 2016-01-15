import cv2
import numpy as np
import sys
from msvcrt import getch
from matplotlib import pyplot as plt

import findFocusImage
import main as app

stepCounter   = 0 # counter of steps
stepNeeded    = 0 # count, how many step u need for next value
gradientValue = 0
nearestImage  = 0 # diff from current image to next
step          = 1 # Stepping Motor step    

imageNames = findFocusImage.imageNames # image path
image = findFocusImage.images # dict that contain image gradient value and path( gradient value = key, path = value)

#step UP to control the stepper motor
def stepUp(event):  
    if event.key == 'up': 
        global gradientValue      
        global stepNeeded
        global nearestImage
        global step

        if(stepNeeded == 0 and gradientValue != findFocusImage.getMinGradientValue()):
            nearestImage = findFocusImage.getDiffFromGradientValue(gradientValue,"UP")
            stepNeeded = nearestImage // step
            print('steps',stepNeeded)
        elif gradientValue == findFocusImage.getMinGradientValue():
            gradientValue = findFocusImage.getMaxGradientValue()
            showImage(image[gradientValue],gradientValue)
        elif stepNeeded >= 10:
            stepNeeded = stepNeeded // 2
            print('steps',stepNeeded)
        else:
            stepNeeded -= 1
            print('steps',stepNeeded)
            if stepNeeded == 0  :
                gradientValue -= nearestImage
                showImage(image[gradientValue],gradientValue)
           
cid = plt.gcf().canvas.mpl_connect('key_press_event', stepUp)
    
#step Down to control the stepper motor
def stepDown(event):
    if event.key == 'down':
        img = cv2.imread(imageNames[1])
        plt.subplot(1,1,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        plt.show() 
cid = plt.gcf().canvas.mpl_connect('key_press_event', stepDown)
    
def main(argv = sys.argv):
    global gradientValue 
    if len(argv) > 1:  
        path = argv[1]+'*.jpg'
        app.loadImages(path) # load an images from directory   
        gradientValue = findFocusImage.getAverageGradientValue()
        nearestImage = findFocusImage.getDiffFromGradientValue(gradientValue,"UP")
        gradientValue -= nearestImage
        showImage(image[gradientValue], gradientValue) 
    else:
        app.loadImages('./*.jpg') # load an images from root
        gradientValue = findFocusImage.getAverageGradientValue()
        nearestImage = findFocusImage.getDiffFromGradientValue(gradientValue,"UP")
        gradientValue -= nearestImage
        showImage(image[gradientValue], gradientValue) 


#clean and set new plot
def plotConfigure():
   plt.cla()
   plt.clf()
   plt.axis("off")


def showImage(image,gradientValue):
    img = cv2.imread(image)
    print("\nCurrent Image", image) 
    print("\nGradient Value", gradientValue) 
    plt.subplot(1,1,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show()         

if __name__ == "__main__": 
   plotConfigure()
   main()
  
   
