"""
    7-Eleven Python CLI
    An example of how to login with the API and add credit to your account via credit card.



"""

import fuellock.lib.account as account
import fuellock.lib.fuellock as fuellock
import requests
import json


def getCheapestFuel(fueltype):
    # Gets the cheapest fuel price for a certain type of fuel and the postcode
    # This is used for the automatic lock in
    r = requests.get("https://projectzerothree.info/api.php?format=json")
    response = json.loads(r.text)
    """
    52 = Unleaded 91
    53 = Diesel
    54 = LPG
    55 = Unleaded 95
    56 = Unleaded 98
    57 = E10
    """
    if fueltype == "52":
        fueltype = 1
    if fueltype == "53":
        fueltype = 4
    if fueltype == "54":
        fueltype = 5
    if fueltype == "55":
        fueltype = 2
    if fueltype == "56":
        fueltype = 3
    if fueltype == "57":
        fueltype = 0

    # Get the postcode and price
    postcode = response["regions"][0]["prices"][fueltype]["postcode"]
    price = response["regions"][0]["prices"][fueltype]["price"]
    latitude = response["regions"][0]["prices"][fueltype]["lat"]
    longitude = response["regions"][0]["prices"][fueltype]["lng"]
    return postcode, price, latitude, longitude


if __name__ == "__main__":
    # The fuel type we want. 56 is premium unleaded
    FUEL_TYPE = "56"

    # The email of all of our accounts
    accounts = [
        "first_email@gmail.com",
        "second_email@gmail.com",
        "third_email@gmail.com",
    ]

    passwords = ["myfirstpassword", "thisispassword2", "andthethirdone"]

    # Combine the username and password together
    for user in zip(accounts, passwords):
        # Login to 7Eleven
        myaccount = account.login(user[0], user[1])

        # Get the cheapest fuel, and work out how much fuel we can lock in
        fuel_location = getCheapestFuel(FUEL_TYPE)
        litres = int(150)

        # Start the lock in session. Here you can confirm the price if you want
        # Note: You need to add the price confirmation yourself.
        fuellock.startLockinSession(
            myaccount[0], myaccount[1], fuel_location[2], fuel_location[3]
        )

        # Lock in the price
        fuellock.confirmLockin(
            myaccount[0], myaccount[1], myaccount[2], FUEL_TYPE, litres
        )

        # And for good measure, just logout again
        account.logout(myaccount[0], myaccount[1])
