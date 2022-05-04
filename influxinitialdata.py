#influxdb and grafana requirements and credentials
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "auz6q4v1Xg-O_vwIfLm0wIHUG-I3L4yhW7lqCtmUUepkrwTaoiKc3XP6dchap9WJpHXCIhiEAHUXuoYLoEmr9g=="
org = "utm"
bucket = "electricalmeter/autogen"

#device 1

#write initial data point at usagebox

usage = 200000 

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
	
    
    write_api = client.write_api(write_options=SYNCHRONOUS)
            
    point = Point("idr_usage") \
      .tag("idr_meter", "idr_meter1") \
      .field("idr_usage", usage) \
      .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket, org, point)
            
#write initial data point at usage

text_int = 1.00

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    
     write_api = client.write_api(write_options=SYNCHRONOUS)
        
     point = Point("kWh") \
       .tag("meter", "meter1") \
       .field("display_usage", text_int) \
       .time(datetime.utcnow(), WritePrecision.NS)

     write_api.write(bucket, org, point)  

#device 2

#write initial data point at usagebox

usage2 = 1 

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
	
    
    write_api = client.write_api(write_options=SYNCHRONOUS)
            
    point = Point("idr_usage") \
      .tag("idr_meter", "idr_meter1") \
      .field("idr_usage", usage2) \
      .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket, org, point)
            
#write initial data point at usage

text_int2 = 1.00

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    
     write_api = client.write_api(write_options=SYNCHRONOUS)
        
     point = Point("kWh") \
       .tag("meter", "meter1") \
       .field("display_usage", text_int2) \
       .time(datetime.utcnow(), WritePrecision.NS)

     write_api.write(bucket, org, point)  
