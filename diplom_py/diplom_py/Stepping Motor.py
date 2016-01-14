import cv2
import numpy as np
import sys
from msvcrt import getch
from matplotlib import pyplot as plt


import findFocusImage
import main as app

imageNames = findFocusImage.imageNames

#step UP to control the stepper motor
def stepUp(event):
    if event.key == 'up':
        img = cv2.imread(imageNames[0])
        plt.subplot(1,1,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        plt.show()         
cid = plt.gcf().canvas.mpl_connect('key_press_event', stepUp)
    
#step Down to control the stepper motor
def stepDown(event):
    if event.key == 'down':
        img = cv2.imread(imageNames[1])
        plt.subplot(1,1,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        plt.show() 
cid = plt.gcf().canvas.mpl_connect('key_press_event', stepDown)
    
    

def main(argv = sys.argv):
     if len(argv) > 1:  
        path = argv[1]+'*.jpg'
        app.loadImages(path) # load an images from directory
     else:
        app.loadImages('./*.jpg') # load an images from root

#clean and set new plot
def plotConfigure():
   plt.cla()
   plt.clf()
   plt.axis("off")
   
   plt.show()

if __name__ == "__main__": 
   main()
   plotConfigure()
   
