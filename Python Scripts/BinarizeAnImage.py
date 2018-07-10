import numpy as np
import matplotlib.pyplot as plt
import cv2

def showResults():
    fig=plt.figure()
    fig.suptitle("ANTIBIOGRAMS", fontsize=16)

    fig2=fig.add_subplot(3,2,1)
    plt.axis("off")
    fig2.title.set_text('RGBimage')
    plt.imshow(RGBimg)


    fig4=fig.add_subplot(3,2,2)
    plt.axis("off")
    fig4.title.set_text('Grayscale')
    plt.imshow(GrayscaleImage, cmap='gray')

    fig4=fig.add_subplot(3,2,3)
    plt.axis("off")
    fig4.title.set_text('BlurredImg')
    plt.imshow(BlurredImage, cmap='gray')

    fig4=fig.add_subplot(3,2,4)
    plt.axis("off")
    fig4.title.set_text('BinarizedImg')
    plt.imshow(BinarizedImg,cmap='gray')
    plt.show()

img = cv2.imread('D:\Alex 2018-2do semestre\Docencia\Antibiograms-project\Antibiograms pictures\Picture 1.jpg')
RGBimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
GrayscaleImage=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
BlurredImage = cv2.medianBlur(GrayscaleImage,9)
ret,BinarizedImg = cv2.threshold(BlurredImage,40,255,cv2.THRESH_BINARY)
showResults()


