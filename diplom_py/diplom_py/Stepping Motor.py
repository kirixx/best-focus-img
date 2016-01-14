import cv2
import numpy as np
import sys
from msvcrt import getch
from matplotlib import pyplot as plt
from matplotlib.widgets import Button

import findFocusImage
import main as app

imageNames = findFocusImage.imageNames

'''fig = plt.figure()
p = fig.add_subplot(111)
p.plot(1,2)'''

#step UP to control the stepper motor
def stepUp(event):
    #global img
    img = cv2.imread(imageNames[0])
    #plt.axis("off")
    plt.subplot(1,1,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    '''cv2.imshow('Image',img)    
    cv2.waitKey(0)
    cv2.destroyWindows()'''

    
#step Down to control the stepper motor
def stepDown(event):
    #global img 
    img = cv2.imread(imageNames[1])
    #plt.axis("off")
    plt.subplot(1,1,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    '''cv2.imshow('Image',img)    
    cv2.waitKey(0)
    cv2.destroyWindows()'''
    
    

def main(argv = sys.argv):
     if len(argv) > 1:  
        path = argv[1]+'*.jpg'
        app.loadImages(path) # load an images from directory
     else:
        app.loadImages('./*.jpg') # load an images from root

if __name__ == "__main__": 
   main()
   plt.cla()
   plt.clf()
   plt.axis("off")
   nextAx = plt.axes([0.9, 0.02, 0.02, 0.04])
   nextBtn = Button(nextAx, '+', color='lightgoldenrodyellow', hovercolor='0.975')
   backAx = plt.axes([0.88, 0.02, 0.02, 0.04])
   backBtn = Button(backAx, '-', color='lightgoldenrodyellow', hovercolor='0.975')
   nextBtn.on_clicked(stepUp)
   backBtn.on_clicked(stepDown)
   plt.show()

   while True:
        key = ord(getch())
        if key == 224: #Special keys (arrows, f keys, ins, del, etc.)
                key = ord(getch())
                if key == 72: #Up arrow
                        print(key)
                        
                elif key == 80: #Down arrow
                        print(key)
                        stepDown(True)
        elif key == 27: #ESC      
                break