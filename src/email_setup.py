import webbrowser
import re
from json import dumps
import os
#Prompts user for credentials
def set_credentials(email,rec_email,password,maxi,mini):
    #Store user data and save it into info.json.
    p_info={
        "sender":email,
        "recipient":rec_email,
        "pswd":password,
        "maxi":maxi,
        "mini":mini,
    }
    with open("src/info.json","w") as file:
        file.write(dumps(p_info))

def prompt_credentials(first_time):
    maxi=input("Enter the maximum price for power, in cents. You will be notified if the price becomes expensive.")
    mini=input("Enter the minimum alert price for power, in cents. You will be notified if the price becomes cheap.")
    rec_email = input("Enter your email address. Alerts will be sent to this email.")
    #If its their first time, the user will have to be guided through setting up a disposable email.
    if first_time:
        ct=1
        signup="https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"
        #This is the step by step guide for how to create a new email.
        with open("email_guide.txt") as file:
            for line in file.readlines():
                print(line, end="")
                input("Press Enter to Continue")
                if ct:
                    webbrowser.open(signup)
                    ct=0
    email=input("Enter the new email address:")
    two_factor="https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome"
    input("Finally, you must enable two-factor authentication to get the app-password. The link will open")
    webbrowser.open(two_factor)
    app_psw="https://myaccount.google.com/u/1/apppasswords"
    input("Finally, you must create an app password. Press enter to open the link. Select \"other\" as your app, and your computer")
    webbrowser.open(app_psw)
    password=input("Enter the app-password:")
    input(f"To confirm, your email is {email} and your password is {password}. Enter to continue. To reset, run reset_creds.py")
    set_credentials(email,rec_email,app_psw,maxi,mini)

if __name__=="main":
    prompt_credentials(True)
    #Checks to make sure the connection can be authenticated
    import debug_smtp
    debug_smtp.debug()
    #Calls send_email each minute by adding it to a crontab.
    location = os.getcwd()
    os.system(f'(crontab -l; echo "* * * * * cd {location}; PYTHONPATH=/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages /usr/local/bin/python3 {location}/src/send_email.py") | crontab -')
