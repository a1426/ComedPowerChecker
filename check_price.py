import requests
class ComedConnectionError(Exception):
    pass
def check_price(min_price,max_price):
    #Reaches out to the Comcast API to check the price
    try:
        req=requests.get("https://hourlypricing.comed.com/api?type=currenthouraverage")
    except requests.exceptions.ConnectionError:
        print("There was an error in trying to reach the website")
        try:
            req=requests.get("https://hourlypricing.comed.com/api?type=currenthouraverage")
        except:
            raise ComedConnectionError("No connection could be made with Comed.")
    price=float(req.json()[0]["price"])
    # Return whether the price is below, above, or at the desired range, respectively.
    if price<min_price:
        return "Below"
    elif price>max_price:
        return "Above"
    else:
        return "At"
