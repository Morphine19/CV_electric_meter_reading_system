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
6. ROI cropping
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

>import cv2 as cv

next we will use video capture to read the video

>cap = cv.VideoCapture('0')

now we create a loop for showing the video .

> while (cap.isOpened()):

to end the loop we will use this command the code basically will break the loop if press the 'q' alphabet

>	if cv.waitKey(25) & 0xFF == ord('q'):
		break

now in the commands we add next wil be added in between the loop 

to Capture frame-by-frame
	
> ret, frame = cap.read()

now to display it we will use cv imshow which is a function to display image 

>cv.imshow('frame', crop)

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







  
  


