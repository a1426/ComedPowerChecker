import requests
class ComedConnectionError(Exception):
    pass
#Comed API, this is where the price is stored.
site="https://hourlypricing.comed.com/api?type=currenthouraverage"
#Simply returns the price, if the website can't be accessed, it raises an error.
def check_price():
    #Reaches out to the Comcast API to check the price
    try:
        req=requests.get(site)
    except requests.exceptions.ConnectionError:
        print("There was an error in trying to reach the website")
        try:
            req=requests.get(site)
        except:
            raise ComedConnectionError("No connection could be made with Comed.")
    price=float(req.json()[0]["price"])
    return price