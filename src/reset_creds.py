from email_setup import prompt_credentials
from json import loads
with open("src/info.json") as file:
    info=loads(file.read(),)
    print("These are your existing credientials:\n"+info)

prompt_credentials(False)