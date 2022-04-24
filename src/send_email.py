import smtplib
from json import loads
import os
from check_price import check_price
import sys
with open("info.json") as file:
    info=loads(file.read())

messages = ["The price for power is now {} the threshold", "The power is at a normal price"]
price = check_price()

if price>float(info["maxi"]):
    relative = "above"
elif price<float(info["mini"]):
    relative = "below"
else:
    relative = "in"
relative="above"
with open("recent_alert.txt", "r+") as f:
    if relative == f.read():
        pass
    else:
        if relative == "in":
            message=messages[1]
        else:
            message=messages[0].format(relative)
        f.seek(0)
        f.write(relative)
        f.truncate()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(info["sender"], info["pswd"])
            server.sendmail(info["sender"], info["recipient"], message)
