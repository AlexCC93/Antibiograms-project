import numpy as np
import matplotlib.pyplot as plt
import cv2

def showResults():
    fig=plt.figure()
    fig.suptitle("ANTIBIOGRAMS", fontsize=16)
    
    fig1=fig.add_subplot(3,2,1)
    plt.axis("off")
    fig1.title.set_text('OriginalImg')
    plt.imshow(img)

    fig2=fig.add_subplot(3,2,2)
    plt.axis("off")
    fig2.title.set_text('RGBimage')
    plt.imshow(RGBimg)

    fig3=fig.add_subplot(3,2,3)
    plt.axis("off")
    fig3.title.set_text('GryascaleImg')
    plt.imshow(GrayscaleImage, cmap='gray')

    fig4=fig.add_subplot(3,2,4)
    plt.axis("off")
    fig4.title.set_text('BlurredImg')
    plt.imshow(filteredImage, cmap='gray')

    fig5=fig.add_subplot(3,2,5)
    plt.axis("off")
    fig5.title.set_text('ResultImg')
    plt.imshow(auxImg)

    fig5=fig.add_subplot(3,2,6)
    plt.axis("off")
    fig5.title.set_text('AntibioticsCircles')
    plt.imshow(auxImg2)
    plt.show()

def detectValidCircles():
    resultArray=np.array([[0,0,0]])             #creates an empty array of 1 row and 3 cols
    for i in circles[0,:]:
        if(filteredImage[i[1],i[0]]>50):         #i[1] corresponds to the columns and i[0] to 
                                                #corresponds to the rows.
            array=np.array([i[0],i[1],i[2]])    #stores that particular element i in an array
            auxArray=array[np.newaxis]          #converting this array into a 1 row and 3 
                                                #cols array
            resultArray=np.append(resultArray,auxArray,axis=0)  #add the auxArray to the
                                                                #final array
    resultArray=np.delete(resultArray,0,0)      #deleting the very first element in the array
    resultArray=resultArray[np.newaxis]         #making it an array of only 1 row
    return resultArray

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

img = cv2.imread('.\Picture 2.jpg')
RGBimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
auxImg=RGBimg.copy()
auxImg2=RGBimg.copy()
filteredImage, GrayscaleImage=imageFilter()
circles = cv2.HoughCircles(filteredImage,cv2.HOUGH_GRADIENT,1,25,param1=50,param2=10,
                           minRadius=38,maxRadius=41)
circles = np.uint16(np.around(circles))
ValidCircles=detectValidCircles()
drawCircles(ValidCircles,auxImg)

antibioticCircles = cv2.HoughCircles(filteredImage,cv2.HOUGH_GRADIENT,1,25,param1=50,param2=10,
                           minRadius=4,maxRadius=10)
antibioticCircles = np.uint16(np.around(antibioticCircles))
drawCircles(antibioticCircles,auxImg2)
showResults()
