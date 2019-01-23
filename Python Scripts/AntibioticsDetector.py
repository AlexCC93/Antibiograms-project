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
    fig4.title.set_text('BlurredImg')
    plt.imshow(filteredImage, cmap='gray')

    fig5=fig.add_subplot(3,2,3)
    plt.axis("off")
    fig5.title.set_text('AntibioticsCircles')
    plt.imshow(auxImg)
    plt.show()

def drawCircles(arrayX, image):
    for i in arrayX[0,:]:
        # draw the outer circle
        cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
def imageFilter():
    GrayscaleImage=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    BlurredImage = cv2.medianBlur(GrayscaleImage,9)
    resultImage=BlurredImage
    return resultImage, GrayscaleImage

img = cv2.imread('.\Picture 6.jpg')#1.jpg')
RGBimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
auxImg=RGBimg.copy()
filteredImage, GrayscaleImage=imageFilter()
antibioticCircles = cv2.HoughCircles(filteredImage,cv2.HOUGH_GRADIENT,1,50,param1=25,param2=10,
                           minRadius=4,maxRadius=10)
antibioticCircles = np.uint16(np.around(antibioticCircles))
drawCircles(antibioticCircles,auxImg)
showResults()
