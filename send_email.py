import smtplib
from email.message import EmailMessage
from json import loads
import os
from initial import location
#NOTE: THIS DOES NOT WORK YET. There is an error with the location, as cron changes the active directory.
with open(location+"/info.json") as file:
    info=(loads(file.read()))
messages = ["The price for power is now {} the threshold at {} cents.","The power has returned to a normal price"]
message=messages[0]
def send_email():
    msg = EmailMessage()
    msg.set_content(message)
    msg['subject'] = "Comed Power Price Alert"
    msg['to'] = info["recipient"]
    msg['from'] = info["sender"]
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(info["sender"], info["pswd"])
    server.send_message(msg)
    server.quit()
send_email()

