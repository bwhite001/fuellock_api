"""
    7-Eleven Python CLI
    An example of how to login with the API and show your current fuel lock.
"""

from fuellock.lib.account import Account as account
from fuellock.lib.fuellock import FuelLock as fuellock
import json

from settings import APP_USERNAME, APP_PASSWORD

if __name__ == "__main__":
    # We need to save the login details into a variable. When you login there are 3 details that 7-Eleven responds
    # with. They are your device secret token, access token and your account id.
    # Device secret and access token are used for almost every request to
    # identify the user as you.
    myaccount = account.login(APP_USERNAME, APP_PASSWORD)

    # Get your last fuel lock(s) into a JSON array.
    get_fuel_locks = json.loads(fuellock.listFuellock(myaccount[0], myaccount[1]))

    # Status codes:
    # 0 = ACTIVE
    # 1 = EXPIRED
    # 2 = REDEEMED
    if get_fuel_locks[0]["Status"] == 2:
        # Get the details of the last fuel lock.
        get_last_lock_details = json.loads(
            fuellock.refreshFplData(myaccount[0], myaccount[1], get_fuel_locks[0]["Id"])
        )

        print(
            "You saved $"
            + str(get_last_lock_details["RewardAmount"])
            + ", while paying "
            + str(get_last_lock_details["CentsPerLitre"])
            + "cents per litre."
        )
        print(
            "You filled up "
            + str(get_last_lock_details["RewardLitres"])[0:5]
            + " litres."
        )

    # And for good measure, logout.
    account.logout(myaccount[0], myaccount[1])
