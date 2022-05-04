from email_setup import set_credentials
from json import loads
with open("src/info.json") as file:
    info=loads(file.read(),)
    print("These are your existing credientials:")
    print(info)
#set_credentials(False)