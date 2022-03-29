import  cv2     as cv 
import  numpy   as np
import pytesseract
from utility import *
import time

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
    crop = frame[300:500,50:1000] 

    #skew correction  
    rotation = rotate(crop)

    #preprocessing
    grasycale_Image = grayscale(rotation)
    threholdimage   = inverse_thresholding(grasycale_Image)
    
    
    
    cv.imshow('frame', threholdimage)

    #tesseract python to image
    custom_config = r' -l digits --psm 7'
    text=pytesseract.image_to_string(threholdimage, config=custom_config)
    text=text.replace(" ","")
    text=text.replace("\n","")
    text=text.replace("\x0c","")
    print(text)


    #delay
    # time.sleep(10)

	# define q as the exit button
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv.destroyAllWindows()