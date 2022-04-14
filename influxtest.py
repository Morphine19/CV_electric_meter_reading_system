from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "auz6q4v1Xg-O_vwIfLm0wIHUG-I3L4yhW7lqCtmUUepkrwTaoiKc3XP6dchap9WJpHXCIhiEAHUXuoYLoEmr9g=="
org = "utm"
bucket = "electricalmeter/autogen"

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
	
	write_api = client.write_api(write_options=SYNCHRONOUS)

	data = "mem,host=host1 used_percent=23.43234543"
	write_api.write(bucket, org, data)


