import webbrowser
import re
ct=1
signup="https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"
with open("email_guide.txt") as file:
    for line in file.readlines():
        print(line, end='')
        input("Press Enter to Continue")
        if ct:
            webbrowser.open(signup)
            ct=0
email=input("Enter the new email address(either the name or the full thing):")
password=input("Enter the new password:")
head=re.search("([a-zA-Z.]*)(@gmail.com)?",email)
email = head.group(1)+"@gmail.com"
input(f"To confirm, your email is {email} and your password is {password}. Enter to continue.")
input("Finally, you must enable Less Secure Apps on your new account. The link will open after you enter.")
webbrowser.open("https://myaccount.google.com/lesssecureapps?pli=1")
input("Once you are done, press enter.")





