import  cv2     as cv 
from    matplotlib import pyplot as plt
import  math
import  numpy   as np
import argparse
import random as rng
import pytesseract
from utility import *

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\ASUS\anaconda3\envs\tesseract\Library\bin\tesseract.exe'


img = cv.imread("C:/Users/ASUS/Desktop/FYP/coding/FYP attempt/IMAGE SAMPLE/template.jpeg")


grayscale_image_2 = grayscale(img)
threshold_image = thresholding(grayscale_image_2)
canny_image_2 = canny(threshold_image)

cv.imshow('1',canny_image_2)

text = pytesseract.image_to_string(canny_image_2)
print(text)



cv.waitKey(0)
cv.destroyAllWindows()