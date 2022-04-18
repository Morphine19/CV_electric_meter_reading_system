# CV_electric_meter_reading_system

# Introduction

This repo contributes to show the process and step by step on my approach to an automated meter reading system for my Final Year Project.The project is titled "IOT BASED MONITORING SYSTEM FOR MULTIPLE SINGLE-PHASE ELECTRICAL METERS" . As mentioned the repo will include the step by step guide so you can also install the system on your single board computer in my case it will be Raspberry pi 3B. Also with every step i will also include a simple video where i demonstrate the task as a my proof of progress.
  
# Flowchart

The Following is the flowchart that ill be using for Iot System, the system is divided to several steps which can see on the image below :
  
  *final flowchart image goes here*
  
As we can see the final flowchart is developed,but this is not the first iteration of the flowchart is a bit diffrent we can it from the image below, tht the unrevised version of the flowchart has a step where we implemented YOLO algorithm to the system but due to the limitation of the project it is concluded that it is better to design the system for a specific single phase electrical meter which is the MSI-200 which is own by the PLN(*pembangkit listrik negara*).This type of meter is really common isntalled among the household in Indonesia.

*comparison between flowchart*

## video

*video goes here*

# Methodology

The Methodology is the part where i show you my progress the system for your own single board compute. I divided the step into 10 steps :

1. install raspbian OS
2. installing OpenCV
3. Accesing the webcam Via OpenCV operators
4. Hardware setup
5. Camera input from the device
6. ROI 
7. Preprocessing
8. Tesseract installation and configuration
9. Installing Influxdb
10. Incoperating influxdb with the system 

without further ado lets get started 

## Install Raspbian OS

There are many single board computer that we can use for the system such as the jetson nano and other types of single board computer,to do so with any types of it we need to install the operating system in my case since im using raspberry pi 3 i will be instll the *raspbian* os.there are several equipments we need in order to prepare ourself for the task.

**the necessities** 

1. raspberry pi 
2. microSD card 
3. monitor keyboard and mouse.
4. Computer with any types of OS (Windows, Mac, linux and even raspbian OS)

first, we need to download and install the raspbian imager from the website

>https://www.raspberrypi.com/software/

second, we need to plug in our microSD card to the computer. you may need to use an adapter or even a card reader if you dont have any memory card slot in your PC.

third, we can now open the installed application and choose raspbian OS , choose your storage device in our case it will be the SD card and finally we can click image and the process of installation will start, this will took you about 10-30 minutes depending on your computer and internet speed. so be patient.....

after finish burnign raspbian to the sd card insert the SD card to the raspberry pi and finally we can run the raspberry pi. after plugging the raspberypi to the monitor you will be prompted with the startup session from raspberry pi where you need to determine your timezone and your credetials which is important.

### Video

*video goes here*

### installing VNC viewer 

depending on your situatuion you may or may not need to use VNC viewer. If you dont know what VNC viewer is basically a remote control access for your computer so that your able to work on your raspi from your pc ,which is more convinient for some people.

to install the vnc viewer first we need to go to the raspbian console and type 

> hostname -I 

what the console will tell us the IP of the raspi that we will use to connect it with the host later.

next, inside the raspbian console type 

> sudo raspi config 

upon opening the sseeting we will go to interfacing access where we can enable VNC. then we can click OK and then click Finish. this system should tell us to reboot our system to adjust the configuration.

now moving on from our raspi to the host computer we need to install the VNC software from here :

> https://www.realvnc.com/en/connect/download/viewer/windows/

upon downloading it we need to install the app then its pretty simple from there.

now you just need to type the internal IP address from the first step and type it on the search bar of VNC viewer application. To know if its works or not you should be prompted with a login window where you need to use your raspi credential if not you may need to retry from the first step.

now you may access your raspi from your own PC. The issue i face while using VNC viewer is the delay which is a bit stressfull but if you have a better internet connection this should not be  problem.

## Installing OpenCV

OpenCV is a library that contain functions that are focused on Computer vision application. To install OpenCV on your raspi its really simple.

first we need to install pip by running the following commands on the raspi terminal 

> mkdir ~/src && cd ~/src
> 
>wget https://bootstrap.pypa.io/get-pip.py
>
>$ sudo python3 get-pip.py

after installing pip we now just have to install the OpenCV by using the following command

>sudo pip install opencv-contrib-python

the console will load and ask do you want to install the following packages just type 'Y' and it should install will no problem.

### video 

*video goes here*


##  Accesing the webcam Via OpenCV operators

### Checking the Camera/webcam

To check if the camera is working properly you may want to do this step, in the raspi console

>sudo apt-get install fswebcam

this is a basic webcam driver that works for most webcam in my case im using Logitech C270

now you can plug in your camera upon plugging it you can again in your console type :

>lsusb

this command show every device connected on your usb port if your device name is listed that means you are ready for the next step

>fswebcam --device your/desired/filepath image.jpg

this should capture an image on the file you mention on command

### Accesing the camera using OpenCV operator in python

now we can start using our opencv operator

in your ide i use genie on raspi

impor the opencv

```
import cv2 as cv
```

next we will use video capture to read the video

```
cap = cv.VideoCapture('0')
```

now we create a loop for showing the video .

```
while (cap.isOpened()):
```

to end the loop we will use this command the code basically will break the loop if press the 'q' alphabet
```
	if cv.waitKey(25) & 0xFF == ord('q'):
		break
```
now in the commands we add next wil be added in between the loop 

to Capture frame-by-frame

```	
	ret, frame = cap.read()
```

now to display it we will use cv imshow which is a function to display image 

```
cv.imshow('frame', crop)
```

now if you done it right you should see the input of the video in python

### video

*viddeo goes here*


## Hardware setup

the setup can be variative depending on your situation and materials you have at hand the following are the pictures of how i setup my device .

*image of device goes here*

whats important is to setup the position of the camera the camera should be facing the electrical meter parallel and the input should be clearly visualizzing the face of the meter. 

Another important point  is setting the focus of the camera you might have to try and readjust your camera focus after multiple times.if your using the same webcam as i do which is the logitech C270 which where the camera focus cannot be adjusted but fortunately we can use a little trick that i follow from the video below.

>https://www.youtube.com/watch?v=4Qo10_REc6U

### video

*video goes here*


## Camera input from the device

This part only shows you the view from my webcam to the device .

*video goes here*

## Tips

Here are 3 tips that can you need to consider while preprocessing the input for Tesseract :

1. The image is in black and white (binarize). and preferably tesseract will read the image better if the text is in the darker color (black) and lighter background (white). 
2. You should leave some space from the image why? necause the system actualy try to detect the empty area therefore we can recieve a better results.
3. Fixing the angle is important, Imagine yourself reading a book in an odd angle it will be hard to read right? similar to tesseract the API will also be confuse and can lead to unwanted results if we dont fix the angle.


## ROI

From the input we reciveve from the video before we are intrested only on recieving the usage box. To do so were going to use several OpenCV functions.

First we open the previous python file (the one we made at 'Accesing the camera using OpenCV operator in python')

then inside the loop and before *cv.imshow* function were going to add several line of codes 

To find the resolution of our video we use the following:

```
 print('resolution',frame.shape)
```

now we can compile and run the code 

in the python console we can see our reolution mine printed

```
resolution (720, 1280, 3)
```

now that we know the resolution of our image we can crop the area were intrested in,to do that :

```
crop = frame [0:720,0:1080]
```

This will crop the video depending on the values that are given in the bracket. and you will need to adjust this accordingly depending on your input and the place of your usage box. Remember the reolution we achieve on the first code that is important since we can register value above it since it will cause an error.

### video

*video goes here*


## Preprocessing

In general preprocessing is *the steps taken to format images before they are used by model training and inference* . To preprocess an image or video in our case its quite variative again depending on what you have as source. We also need to consider the tips i write because itll help us significantly. Since the topic of preprocessing is so broad i will only discuss the function i used in my system. 

To easily use the preprocessing function i create another python file called utility.py. since the function we will be using has several paramater that we can freely adjust it is a good habit to do this and create 'def' for each function so we can easily adjust the parameter from the function and keep our main.py neat.


### Rotating the image

by following the tips we have it ill start by addressing the angle since mine input video is a bit tilted ill be using the following function :

```
def rotate(image):

    src=image
    
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

   
    angle = 2
    M = cv.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv.warpAffine(image, M, (w, h))

    return rotated
```

to clarify the code above here is a short explanation of the code :

the following code basically help us to determine the center of the image this step is important because we ant to rotate the image from its center


```
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    
```

the next part of the is divided into 2 part the cv.geRotationMatrix2D is used to make the transformation matrix M which will be used for rotating a image
then the cv.warpAfine is used to rotate the image referring to the rotation matrix 
(within the function there is a variable *angle* we adjust the values depending on what values you need)

```
    angle = 2
    M = cv.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv.warpAffine(image, M, (w, h))
```

### grayscale an image/video

The next step we will be grayscaling the image, because considering the following step which is the preprocessing the thresholding. The purpose of grayscaling an image or video in a computer vision setup is to decreases processing needs and simplifies the algorithm Color adds to the model's complexity by supplying unneeded information.

here are the function we use to grayscale an image to :

```
def grayscale(image) :
    src = image
    
    type=r'cv.COLOR_BGR2GRAY'
    gray = cv.cvtColor(src,type)

    return gray
```

The code to covert the image to graysclae is really simple we use cv.cvtColor function then we added the source which is our video input and set the color to cv.COLOR_BGR2GRAY which converts the color from BGR which is the normal color format from opencv to grayscale.


### Thresholding an image/video
  
the next  and final preprocessing step is the thresholding,Thresholding is a segmentation technique, used for separating an object considered as a object from its background.There are many types of thresholding but to implement it we are using the same code :

```
def thresholding(image):
    src =image
    thresholdValue =  155
    maxVal = 255

    ret,thresh = cv.threshold(src, thresholdValue, maxVal, cv.THRESH_BINARY ) 
    
    return thresh
```
the most important value to adjust when you're thresholding is to adjust the thresholValue variable, you can start with 100 and add more if your object is still unclear and decrease it when the it when it started to detected noises.

as a side note in the code i use a diffrent type of thresholding which is the inverse thresholding, the result is the reverse of the normal result which will make the object is darker color and white background which is recomendded it the tips section.You may need to adjust the type to thresholding depending on what type of object your working with for more info on thresholding this is the website you can refer  to :

>https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/

### video

*video goes here*


## Tesseract installation and configuration

Tesseract is an OCR(optical character recognition engine) that is developed by google.

### installation

This installation guide is for installing TesseractOCR in raspbian OS.

in the raspbian OS console type :

> sudo apt install tesseract OCR

this will install the tesseract main API,next were going to install the python wrapper for tesseract:

>sudo pip install pytesseract

if you want to ensure that tesseract you can run the following command and it will show you that tesseract installed with its version

>tesseract --version

### tesseract configuration

since we have done the preprocessing for the image this step will be really simple :

first we need to import the tesseract to our system :

```
import pytesseract
```

now inside the loop where we preprocessed the image we  can add the image.to.string syntax. this syntax is the default command use to convert an image inside a image.  

```
custom_config = r' -l digits --psm 7'
text=pytesseract.image_to_string(threholdimage, config=custom_config)
print(text)
```

The image to string syntax takes 2 variable which is the source which will be our preprocessed video and the config, there are alost of configuration you can use for this what i used is 2 really simple configuration which is `-l digits` to set tesseract to only expect numeric value and `--psm 7` psm Page Segmentation Modes, there are many type of segmentation mode you can set the system to,particularly psm 7 sets the tesseract to detect in a sigle word in a single line.


![result](https://user-images.githubusercontent.com/75777945/163777073-5c504f76-58e7-4500-a35a-deac862434c2.JPG)

from the results we can see that there is a space and a ♀ symbol in between the readings,this actually how tesseract marks between readings by giving a page sement with the following symbol to remove the symbol we can use the following code to replace the space and the symbol to a void value.

```
    text=text.replace(" ","")
    text=text.replace("\n","")
    text=text.replace("\x0c","")
```

place the following code before the printing the image and you have a clear readingg without any interuptions. 

As a side note if you want to know how i know which value to replace with the void value i use `repr` before the `print(repr(text))` to represent the returns printable representation of the given object.

### video 

*video goes here*

## Installing Influxdb 

to install ifuxdb here are the following steps inside the raspbian OS terminal :

first we meed to copy the influxdb repo key

>curl https://repos.influxdata.com/influxdb.key | gpg --dearmor | sudo tee /usr/share/keyrings/influxdb-archive-keyring.gpg >/dev/null

Now that we have the InfluxDB repository key installed to our Raspberry Pi, we will need to go ahead and add its repository to the sources list

>echo "deb [signed-by=/usr/share/keyrings/influxdb-archive-keyring.gpg] https://repos.influxdata.com/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

now thats done we can now install infludb

> sudo apt install influxdb

now that influxdb is successfully installed we can set the enable and start the server 

>sudo systemctl unmask influxdb
>sudo systemctl enable influxdb
>sudo systemctl start influxdb

now that we have installed influxdb we just have to access it by typing `http://localhost:8086`  in your *BROWSER* not console.

if theres no problem you should be prompted with the influxdb page and now what you have to is just to sign in or sign up.


### video

*video goes here*

## Incoperating influxdb with the system 
