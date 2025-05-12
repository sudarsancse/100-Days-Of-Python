import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
up_down = None

load_dotenv()
##--------------------Env values-------------------##
stock_api_key = os.getenv("ALPHA_VANTAGE_STOCK_API_KEY")
new_api_key = os.getenv("NEWS_APY_KEY")
my_number = os.getenv("MY_NUMBER") ## reciver sms number

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

##--------------------links-------------------##
link = "https://www.alphavantage.co/query?"
news_link = "https://newsapi.org/v2/everything?"

stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_api_key
}

stock_price = requests.get(url=link, params=stock_parameters)
print(stock_price.raise_for_status())
data = stock_price.json()["Time Series (Daily)"]

all_dates = [ value for (key, value) in data.items()]

yesterday_data = all_dates[0]
day_before_yesterday_data = all_dates[1]

yesterday_data_cls_price = yesterday_data["4. close"]
day_before_yesterday_data_cls_price=day_before_yesterday_data["4. close"]

diff = float(yesterday_data_cls_price) - float(day_before_yesterday_data_cls_price)

if diff > 0:
    up_down = "🔺"
else:
    up_down ="🔻"

diff_persent = round((diff / float(yesterday_data_cls_price)) *100)

if abs(diff_persent) > 5:
    ## STEP 2: Use https://newsapi.org
    news_parameters={
    "apikey":new_api_key,
    "qinTitle":COMPANY_NAME
}
    news_res = requests.get(url=news_link,params=news_parameters)
    news_res.raise_for_status()
    news_data = news_res.json()['articles']
    three_artical = news_data[:3]
    formated_artical = [f"{STOCK}: {up_down}{diff_persent}% \nHeadline: {artical['title']}. \nBrief: {artical['description']}" for artical in three_artical]

    ## STEP 3: Use https://www.twilio.com
    client = Client(account_sid, auth_token)
    for artical in formated_artical:
        message = client.messages.create(
        body=artical,
        from_="+18574206826",
        to=f"+91{my_number}",
    )

