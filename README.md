# ComedPowerChecker
# Purpose
The purpose of this repository is to inform Comed users when their price rises above or falls below a certain threshold, checked every hour.
The user will be notified when the threshold is crossed, and when it returns to normal, so that they will not be excessively alerted.

# Guide
To setup this program, the user should first run email_setup.py.
This program first prompts the user on their thresholds, and then guides them through setting up a disposable gmail account that is able to be accessed by SMTPlib, so that their personal email may be notified.
If one wants to change their credentials, they should run reset_creds.py.
