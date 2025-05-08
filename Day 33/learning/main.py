import requests
from dotenv import load_dotenv
import os

# res = requests.get(url="http://api.open-notify.org/iss-now.json")
# res.raise_for_status()
# longitude = res.json()["iss_position"]["longitude"]
# latitude = res.json()["iss_position"]["latitude"]
# iss_position = (latitude, longitude)
# print(iss_position )


##-----------------------------------SUN RISE API------------------------------------##

my_lat = os.getenv("MY_LATITUDE")
my_lng = os.getenv("MY_LONGITUDE") 


parameters = {
    "lat":my_lat,
    "lng":my_lng,
    "formatted":0
}

req = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
req.raise_for_status()
data = req.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]
print(sunset)
