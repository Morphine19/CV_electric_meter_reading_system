# importing the necessary libraries
import cv2 as cv
import numpy as np
from utility import *


# Creating a VideoCapture object to read the video
cap = cv.VideoCapture(0)


# Loop until the end of the video
while (cap.isOpened()):

	# Capture frame-by-frame
	ret, frame = cap.read()

    #preprocessing goes here (edit frame variable)
	

	cv.imshow('frame', frame)
	# define q as the exit button
	if cv.waitKey(25) & 0xFF == ord('q'):
		break

# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv.destroyAllWindows()

