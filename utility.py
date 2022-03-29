from turtle import ScrolledCanvas
import  cv2     as cv 
from    matplotlib import pyplot as plt
import  math
import  numpy   as np
import argparse
import random as rng
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\ASUS\anaconda3\envs\tesseract\Library\bin\tesseract.exe'


#reading images

source = cv.imread('C:/Users/ASUS/Desktop/FYP/coding/FYP attempt/IMAGE SAMPLE/template.jpeg')

# cv.imshow('original',source)

#preprocessing 

#resizing image
#syntax : cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])

def resize(image) :
    
    src = image                                     #adding the image to the source
    x = int(500)                                    #image size
    y = int(500)
    resize_image = cv.resize( src, (x,y) , interpolation = cv.INTER_CUBIC  )   #syntax for resizing
    # cv.imshow('resized',resize_image)
   
    return  resize_image

#Bilateral filter to focus on object
#applies blur but retain the main focus of the objecct
#cv2.bilateralFilter ( src, dst, d, sigmaColor,sigmaSpace, borderType = BORDER_DEFAULT )


def bilateral_filter(image) :

    src = image
    diameter    = 5
    sigma_color = 10
    sigma_space = 10

    bilateral = cv. bilateralFilter(src, diameter , sigma_color, sigma_space )

    return bilateral

    

#convert image to grayscale 

def grayscale(image) :
    src = image

    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

    return gray



#grayscaled image histogram

def gray_histogram(image) :
    src = image

    gray_hist = cv.calcHist([src], [0] , None , [256] , [0,256] )

    plt.figure()
    plt.title('grayscale histogram')
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_hist)
    plt.xlim([0,256])
    plt.show()

    return



#Colored image histogram

def coloured_histogram(image):

    # generating histogram for Histogram equalization
    src = image

    hist = cv.calcHist([src], [0] , None , [256] , [0,256] )

    plt.figure()
    plt.title('color histogram')
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    colors = ('b', 'g' , 'r')
    for i, col in enumerate(colors):
        hist = cv.calcHist([src], [i],None , [256] , [0,256])
        plt.plot(hist, color = col)
        plt.xlim([0,256])

    plt.show()

    return



#CLAHE (Contrast Limited Adaptive Histogram Equalization)


def clahe(image):
    src = image

    clip_limit = 3

    #tile grid size
    x = 25
    y = 25

    clahe = cv.createCLAHE(clipLimit = clip_limit , tileGridSize=(x,y))
    cl_img = clahe.apply(src)
    

    return cl_img



#canny for edge detection
#Canny(image, threshold1, threshold2)

def canny(image):
     src = image
     threshold1 = 100
     threshold2 = 200
    
     edge = cv.Canny(src, threshold1, threshold2)

     return edge

#hough transform to detect line

def hough_transform(image):
    src = image 

    cdst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    rho = 1
    theta =np.pi / 180
    threshold = 150

    

    lines = cv.HoughLines(src, rho, theta, threshold, None, 0, 0)  


    # to draw the lines on the picture
    if lines is not None:
     for i in range(0, len(lines)):

        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))

        lined_image = cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)



    return lined_image

def erosion(image):
    src = image
    kernel = np.ones((5,5), np.uint8) 
    iterations_num = 1

    erosion = cv.erode(src,kernel, iterations = iterations_num)

    return erosion

def dilation(image):
    src = image
    kernel = np.ones((3,3), np.uint8) 
    iterations_num = 1

    dilation = cv.dilate(src,kernel, iterations = iterations_num)  

    return dilation

def thresholding(image):
    src =image
    thresholdValue =  155 #93
    maxVal = 255

    ret,thresh = cv.threshold(src, thresholdValue, maxVal, cv.THRESH_BINARY ) 
    
    return thresh

def inverse_thresholding(image):
    src =image
    thresholdValue =  170 #93
    maxVal = 255

    ret,inversethresh = cv.threshold(src, thresholdValue, maxVal, cv.THRESH_BINARY_INV ) 
    
    return inversethresh

def adaptive_thresholding(image):
    src = image
    blockSize = 199
    constant =  5

    adaptive = cv.adaptiveThreshold(src, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,blockSize ,constant)
    
    return adaptive

def otsu_thresholding(image):
    src= image
    thresholdValue=200
    maxVal = 255
    
    ret,otsu = cv.threshold(src, thresholdValue, maxVal, cv.THRESH_BINARY + cv.THRESH_OTSU)

    return otsu


#image increase contrast/brightness
def contrast(image):

    src = image
    alpha = 1 # Contrast control (1.0-3.0)
    beta = 0 # Brightness control (0-100)
    adjusted = cv.convertScaleAbs(src, alpha=alpha, beta=beta)

    return adjusted

#denoise module fastNImeansdenoising

def fastDenoise(image):

    src = image

    h_luminance = 3
    photo_render = 3
    search_window = 7
    block_size = 21

    denoise = cv.fastNlMeansDenoisingColored(src,None,h_luminance,photo_render,search_window,block_size,)

    return denoise

#rotating image with adjsutable image for skewing image

def rotate(image):

    src=image
    
    # grab the dimensions of the image and calculate the center of the image
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # rotate our image by -90 degrees around the image
    angle = 2
    M = cv.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv.warpAffine(image, M, (w, h))

    return rotated


def OCRin(image):

    src=image
    custom_config = r' -l digits -c page_separator= --psm 7'
    ocr = pytesseract.image_to_string(src, config=custom_config )
    ocr=ocr.replace(" ","")
    ocr=ocr.replace("\n","")
    ocr=ocr.replace("\x0c","")
    return ocr

#------------------------------------------------------------------------------------------------------------------------------------------------------------#


#preprocessing with erosion


# blur_image  = bilateral_filter(source)
# grayscale_image = grayscale(blur_image)
# erosion_image = erosion(grayscale_image)
# canny_image = canny(erosion_image)



# cv.imshow('1',blur_image)
# cv.imshow('2',grayscale_image)
# cv.imshow('3',erosion_image)
# cv.imshow('4',canny_image)

#preprocessing with thresholding

# grayscale_image_2 = grayscale(source)
# threshold_image = thresholding(grayscale_image_2)
# canny_image_2 = canny(threshold_image)

# cv.imshow ('1 thresh',grayscale_image_2)
# cv.imshow('2 thresh',threshold_image)
# cv.imshow('3 thresh',canny_image_2)

#preprocessing with adaptive thresholding 

# grayscale_image_3 = grayscale(source)
# adaptive_threshold_image = adaptive_thresholding(grayscale_image_3)
# canny_image_3  = canny(adaptive_threshold_image)

# cv.imshow ('1 Adapt thresh',grayscale_image_3)
# cv.imshow('2 Adapt thresh',adaptive_threshold_image)
# cv.imshow('3 Adapt thresh',canny_image_3)


cv.waitKey(0)