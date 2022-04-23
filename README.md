# ComedPowerChecker
# Purpose
The purpose of this repository is to inform Comed users when their price rises above or falls below a certain threshold, checked every hour.
The user will be notified when the threshold is crossed, and when it returns to normal, so that they will not be excessively alerted.

# Description and Guide
The user should first run email_setup.py.
This program first prompts the user on their thresholds, and then guides them through setting up a disposable gmail account that is able to be accessed by SMTPlib, so that their personal email may be notified. It saves the data in a .json file, and then runs a diagnostic test to make sure that the smtp.gmail.com server can be accessed. If it can't, it runs some code to install a module that allows the connection to happen. The installation code is not mine, all of it can be found at [this github page](https://github.com/python/cpython/blob/main/Mac/BuildScript/resources/install_certificates.command).
Following the setup, the program then adds a cronjob that runs another program every hour. This program requests the price from the Comed API, and checks whether the price is outside of the threshold. If it is, it sends an alert email, and changes relative.txt, to show that the last alert was outside of the threshold. The next hour, it will check whether the price is outside of the threshold. If it is, it will not send an alert, as one has already been sent. If it isn't, it will send an alert that the price has gone back to normal.
