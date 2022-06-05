import smtplib
from json import loads
from xdrlib import ConversionError
from check_price import check_price
#Read the user's data from info.json, namely the tresholds, emails, and passwords
with open("src/info.json") as file:
    info=loads(file.read())

messages = ["The price for power is now {} the threshold", "The power is at a normal price"]
#Gets the price and checks it
price = check_price()
if price>float(info["maxi"]):
    relative = "above"
elif price<float(info["mini"]):
    relative = "below"
else:
    relative = "in"
#Opens the recent_alert document and reads it. This document contains the most recent alert.
#This is done to prevent the user from the same alert each minute, and only sends an email once the alert changes.
with open("src/relative.txt", "r+") as f:
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