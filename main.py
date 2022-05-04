#computer vision requirements
import  cv2     as cv 
import pytesseract
from utility import *
import time

#influxdb and grafana requirements and credentials
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "auz6q4v1Xg-O_vwIfLm0wIHUG-I3L4yhW7lqCtmUUepkrwTaoiKc3XP6dchap9WJpHXCIhiEAHUXuoYLoEmr9g=="
org = "utm"
bucket = "electricalmeter/autogen"


# Creating a VideoCapture object to read the video
cap = cv.VideoCapture(0)


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
    crop = frame[100:200,100:550] 
 

    #skew correction  
    rotation = rotate(crop)

    #preprocessing
    grasycale_Image = grayscale(rotation)
    
    thresholdimage   = inverse_thresholding(grasycale_Image)
    
    #cv.imshow('frame', thresholdimage)

    #tesseract python to image
    custom_config = r'-l digits --psm 7'
    text=pytesseract.image_to_string(thresholdimage, config=custom_config)
    text=text.replace(" ","")
    text=text.replace("\n","")
    text=text.replace("\x0c","")
    text=text.replace(".","")
    
    text_int = int(text)
    limit = 999999
    if text_int <= limit:
        print("displayed"+" "+ text +" "+ "kWh")
    else :
        continue
        
        
    
    #influxdb data send
    
    with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    
        write_api = client.write_api(write_options=SYNCHRONOUS)
        
        point = Point("kWh") \
          .tag("meter", "meter1") \
          .field("display_usage", text_int) \
          .time(datetime.utcnow(), WritePrecision.NS)

        write_api.write(bucket, org, point)
        
    #calcualtion for usage
    #starting=
    #perkwh  = 1444.70
     
        #query for comparing both data
        query_api = client.query_api()
        
        #note :change query1 range to 1d 
        query1 = ' from(bucket:"electricalmeter/autogen")\
        |> range(start: -5m)\
        |> filter(fn:(r) => r._measurement == "kWh")\
        |> filter(fn: (r) => r._field == "display_usage")\
        |> filter(fn:(r) => r.meter == "meter1" ) \
        |> last()'

        #query2 = ' from(bucket:"electricalmeter/autogen")\
        #|> range(start: -1m)\
        #|> filter(fn:(r) => r._measurement == "kWh")\
        #|> filter(fn: (r) => r._field == "display_usage")\
        #|> filter(fn:(r) => r._meter == "meter1" )\
        #|> last()'
        
        result1 = client.query_api().query(org=org, query=query1)
        results1 = []
        for table in result1:
            for record in table.records:
                results1.append(record.get_value())
        #print(results1[0])
        
        #result2 = client.query_api().query(org=org, query=query2)
        #results2 = []
        #for table in result2:
        #    for record in table.records:
        #        results2.append(record.get_value())
        #print(results2[0])
        
        #diffrence between usage real time
        #diff = results2[0]-results1[0]
        
        #diffrence in adjusted time 
        #202800-(622.969/1444.70)
        #202880- 431
        
        diff  =  results1[0] - 202449
        
        usage = diff * 1444.70
        
        print(usage)
        
        #write usage to a new point at influxdb database
        with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    
            write_api = client.write_api(write_options=SYNCHRONOUS)
            
            point = Point("idr_usage") \
              .tag("idr_meter", "idr_meter1") \
              .field("idr_usage", usage) \
              .time(datetime.utcnow(), WritePrecision.NS)

            write_api.write(bucket, org, point)
    
    #delay
    time.sleep(60)

	# define q as the exit button
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv.destroyAllWindows()




