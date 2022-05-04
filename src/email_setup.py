import webbrowser
import re
from json import dumps
import os
def set_credentials(first_time):
    maxi=input("Enter the maximum price for power, in cents. You will be notified if the price becomes expensive.")
    mini=input("Enter the minimum alert price for power, in cents. You will be notified if the price becomes cheap.")
    rec_email = input("Enter your email address.")
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
    email=input("Enter the new email address(either the name or the full thing):")
    password=input("Enter the new password:")
    head=re.search("([a-zA-Z0-9.]*)(@gmail.com)?",email)
    email = head.group(1)+"@gmail.com"
    input(f"To confirm, your email is {email} and your password is {password}. Enter to continue. To reset, run reset_creds.py")
    input("Finally, you must enable Less Secure Apps on your new account. Sign in to it and the link will open after you enter.")
    webbrowser.open("https://myaccount.google.com/lesssecureapps?pli=1")
    input("Once you are done, press enter.")
    p_info={
        "sender":email,
        "recipient":rec_email,
        "pswd":password,
        "maxi":maxi,
        "mini":mini,
    }
    with open("info.json","w") as file:
        file.write(dumps(p_info)) 
if __name__="main":
    set_credentials(True)
    import debug_smtp
    debug_smtp.debug()
    location = os.getcwd()
    os.system(f'(crontab -l; echo "* * * * * cd {location}; PYTHONPATH=/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages /usr/local/bin/python3 {location}/src/send_email.py") | crontab -')
