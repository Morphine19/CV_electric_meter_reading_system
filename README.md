# CV_electric_meter_reading_system

## Introduction

This repo contributes to show the process and step by step on my approach to an automated meter reading system for my Final Year Project.The project is titled "IOT BASED MONITORING SYSTEM FOR MULTIPLE SINGLE-PHASE ELECTRICAL METERS" . As mentioned the repo will include the step by step guide so you can also install the system on your single board computer in my case it will be Raspberry pi 3B. Also with every step i will also include a simple video where i demonstrate the task as a my proof of progress.
  
## Flowchart

The Following is the flowchart that ill be using for Iot System, the system is divided to several steps which can see on the image below :
  
  *final flowchart image goes here*
  
As we can see the final flowchart is developed,but this is not the first iteration of the flowchart is a bit diffrent we can it from the image below, tht the unrevised version of the flowchart has a step where we implemented YOLO algorithm to the system but due to the limitation of the project it is concluded that it is better to design the system for a specific single phase electrical meter which is the MSI-200 which is own by the PLN(*pembangkit listrik negara*).This type of meter is really common isntalled among the household in Indonesia.

*comparison between flowchart*


## Methodology

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

### Install Raspbiam OS

There are many single board computer that we can use for the system such as the jetson nano and other types of single board computer,to do so with any types of it we need to install the operating system in my case since im using raspberry pi 3 i will be instll the *raspbian* os.there are several equipments we need in order to prepare ourself for the task.
**the necessities** 
1. raspberry pi 
2. microSD card 
3. monitor keyboard and mouse.
4. Computer with any types of OS (Windows, Mac, linux and even raspbian OS)

first, we need to download and install the raspbian imager from the <a href="https://www.raspberrypi.com/software/" target="_blank">here</a>. 

second, we need to plug in our microSD card to the computer. you may need to use an adapter or even a card reader if you dont have any memory card slot in your PC.

third, we can now open the installed application and choose raspbian OS , choose your storage device in our case it will be the SD card and finally we can click image and the process of installation will start, this will took you about 10-30 minutes depending on your computer and internet speed. so be patient.....

after finish burnign raspbian to the sd card insert the SD card to the raspberry pi and finally we can run the raspberry pi. after plugging the raspberypi to the monitor you will be prompted with the startup session from raspberry pi where you need to determine your timezone and your credetials which is important.


#### installing VNC viewer 

depending on your situatuion you may or may not need to use VNC viewer. If you dont know what VNC viewer is basically a remote control access for your computer so that your able to work on your raspi from your pc ,which is more convinient for some people.

to install the vnc viewer first we need to go to the raspbian console and type ' hostname -I ',what the console will tell us the IP of the raspi that we will use to connect it with the host later.

next, inside the raspbian console type *sudo raspi config* upon opening the sseeting we will go to interfacing access where we can enable VNC. then we can click OK and then click Finish. this system should tell us to reboot our system to adjust the configuration.






  
  


