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
    plt.imshow(filteredImage,'gray')

    fig5=fig.add_subplot(3,2,5)
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
    ret,BinarizedImg = cv2.threshold(BlurredImage,40,255,cv2.THRESH_BINARY)
    resultImage=BinarizedImg
    return resultImage, BlurredImage, GrayscaleImage

img = cv2.imread('D:\Alex 2018-2do semestre\Docencia\Antibiograms-project\Antibiograms pictures\Picture 1.jpg')
RGBimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
auxImg=RGBimg.copy()
filteredImage, BlurredImage, GrayscaleImage=imageFilter()
antibioticCircles = cv2.HoughCircles(filteredImage,cv2.HOUGH_GRADIENT,1,50,param1=25,param2=10,
                           minRadius=4,maxRadius=10)
antibioticCircles = np.uint16(np.around(antibioticCircles)) #this is an array of
                            #(1,11,3) shape, where the last dimension is of 3
                            #because it contains the center coordinate and the
                            #radius of the circle encountered.
drawCircles(antibioticCircles,auxImg)
diametersArray=np.array([0,0,0])[np.newaxis] 
for i in range (0,antibioticCircles.shape[1]):
    centerPoint=antibioticCircles[0,i]
    centerPointX=centerPoint[0]
    centerPointY=centerPoint[1]
    pillRadius=centerPoint[2]
    pixValue=filteredImage[centerPointY,centerPointX]
    filsIndex=centerPointY
    auxCounter=0
    distanceToBottom=0
    distanceToTop=0
    while(pixValue>125):
        filsIndex=filsIndex+1
        pixValue=filteredImage[filsIndex,centerPointX]
    while(pixValue<125):
        distanceToBottom=distanceToBottom+1
        filsIndex=filsIndex+1
        pixValue=filteredImage[filsIndex,centerPointX]
    distanceToBottom=distanceToBottom+pillRadius
    filsIndex=centerPointY  
    while(pixValue>125):
        filsIndex=filsIndex-1
        pixValue=filteredImage[filsIndex,centerPointX]
    while(pixValue<125):
        distanceToTop=distanceToTop+1
        filsIndex=filsIndex-1
        pixValue=filteredImage[filsIndex,centerPointX]
    distanceToTop=distanceToTop+pillRadius
    distanceDifference=abs(distanceToBottom-distanceToTop)
    if(distanceDifference<6):
        officialRadius=(distanceToBottom+distanceToTop)/2
    else:
        officialRadius=min(distanceToBottom,distanceToTop)
    auxArray=np.array([centerPointX, centerPointY, officialRadius*2])[np.newaxis]
    diametersArray=np.append(diametersArray,auxArray,axis=0)
diametersArray=np.delete(diametersArray,diametersArray[0,:],axis=0)
showResults()
