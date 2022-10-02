import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()

gmail = "tr633064@gmail.com"
gmail_password = "aampvujzzotxxdio"
yahoo = "tr633064@yahoo.com"
letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

df = pandas.read_csv("birthdays.csv")
for i in range(len(df)):
    if df.loc[i, "month"] == now.month and df.loc[i, "day"] == now.day:
        random_letter = random.choice(letter_list)
        with open(random_letter) as file:
            data = file.read()
            new_data = data.replace("[NAME]", df.loc[i, "name"])

        with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
            gmail_connection.starttls()
            gmail_connection.login(user=gmail, password=gmail_password)
            gmail_connection.sendmail(from_addr=gmail, to_addrs=df.loc[i, "email"],
                                      msg=f"Subject:Happy Birthday!\n\n{new_data}")
