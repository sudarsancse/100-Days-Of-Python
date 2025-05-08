import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os
import time

my_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SENDER_EMAIL_PASSWORD")
rc_email = os.getenv("RECIVER_EMAIL")

MY_LAT = os.getenv("MY_LATITUDE") # Your latitude
MY_LONG =os.getenv("MY_LONGITUDE")  # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude<= MY_LONG+5 :
        return True
    

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smpt.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=rc_email, msg="Subject:Look Up☝️\n\nTHe ISS is above you in the Sky.")


