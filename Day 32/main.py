# import os
# import smtplib
# from dotenv import load_dotenv

# load_dotenv()

# my_gmail = os.getenv("SENDER_EMAIL")
# my_password =os.getenv("SENDER_EMAIL_PASSWORD")
# rc_email = os.getenv("RECIVER_EMAIL")

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_gmail, password=my_password)
#     connection.sendmail(from_addr=my_gmail, to_addrs=rc_email, msg="SUbject:Hello\n\nThis is my new email")
    

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# dath_of_barth = dt.datetime(month=7, day=4, year=2000)
# print(dath_of_barth)


# import random
# import os
# import smtplib
# import datetime as dt
# from dotenv import load_dotenv

# load_dotenv()
# my_email = os.getenv("SENDER_EMAIL")
# password = os.getenv("SENDER_EMAIL_PASSWORD")
# rec_email = os.getenv("RECIVER_EMAIL")

# now = dt.datetime.now()
# day=now.weekday()
# if day == 0 :
#     with open("quotes.txt" , "r") as sms:
#         new_sms =random.choice(sms.readlines())

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs=rec_email, msg=f"Subject: For monday\n\n{new_sms}")


##-------------------------------MAIN PROJECT--------------------------------##
import random
import os
import pandas
import smtplib
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SENDER_EMAIL_PASSWORD")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{contents}")


