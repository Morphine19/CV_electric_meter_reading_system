import  cv2     as cv 


#convert image to grayscale 

def grayscale(image) :
    src = image

    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

    return gray


def inverse_thresholding(image):
    src =image
    thresholdValue =  170 #93
    maxVal = 255

    ret,inversethresh = cv.threshold(src, thresholdValue, maxVal, cv.THRESH_BINARY_INV ) 
    
    return inversethresh



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
