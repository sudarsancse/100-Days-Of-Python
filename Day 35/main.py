import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

link = "https://pro.openweathermap.org/data/2.5/forecast"

my_lat = os.getenv("MY_LATITUDE")
my_lon = os.getenv("MY_LONGITUDE")
my_api_key = os.getenv("WEATHER_API_KEY")
my_number = os.getenv("MY_NUMBER") ## reciver sms number

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

weather_parameters ={
    "lat" : my_lat,
    "lon": my_lon,
    "appid":my_api_key,
    "cnt":4
}

res = requests.get(url=link, params=weather_parameters)
print(res.raise_for_status())
data = res.json()

# print(data["list"][1]["weather"][0]["main"])

will_rain = False
for hour_data in data["list"]:
    condition_code =hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="it's going to rain🌧️ today . Rember to bring Umbrella☔",
    from_="+18574206826",
    to=f"+91{my_number}",
)
    print(message.status)




