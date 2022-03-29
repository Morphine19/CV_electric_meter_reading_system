from ast import Mod
from lib2to3.pytree import _Results
from ssl import OP_NO_COMPRESSION
from tkinter import Frame
from turtle import ScrolledCanvas


import  cv2     as cv 
from    matplotlib import pyplot as plt
import  math
import  numpy   as np
import argparse
import pytesseract
from utility import *

#import tesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\ASUS\anaconda3\envs\tesseract\Library\bin\tesseract.exe'

# Creating a VideoCapture object to read the video
cap = cv.VideoCapture('C:/Users/ASUS/Desktop/FYP/coding/FYP attempt/IMAGE SAMPLE/vid sample 20220324.mp4')


# Loop until the end of the video
while (cap.isOpened()):

	# Capture frame-by-frame
    ret, frame = cap.read()

    #zooming (cropping only the required area )

    # Check the type of read image
    # print(type((frame)))

    # Check the shape of the input image
    #Shape of the image (720, 1280, 3)
    # print("Shape of the image", frame.shape) 

    # [rows, columns]
    #just usage box [300:500,50:1100] 
    crop = frame[300:500,50:1100] 

    #skew correction  
    rotate_image = rotate(crop)

    #preprocesing
    grayscale_image =grayscale(rotate_image)

    #boxing each digit
    digit1  = grayscale_image[0:200,0:200]  
    digit2  = grayscale_image[0:200,250:350]
    digit3  = grayscale_image[0:200,350:500]
    digit4  = grayscale_image[0:200,550:630]
    digit5  = grayscale_image[0:180,700:790]
    digit6  = grayscale_image[0:180,800:950]

    
    #cv.imshow('digit1',digit1)


    #tesseract python to image
    OCRdigit1 = OCRin(digit1)
    OCRdigit2 = OCRin(digit2)
    OCRdigit3 = OCRin(digit3)
    OCRdigit4 = OCRin(digit4)
    OCRdigit5 = OCRin(digit5)
    OCRdigit6 = OCRin(digit6)

    #printing results
    results = OCRdigit1+OCRdigit2+OCRdigit3+OCRdigit4+OCRdigit5+OCRdigit6
    print(results)

	# define q as the exit button
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv.destroyAllWindows()