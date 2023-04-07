"""
    7-Eleven Python CLI
    An example of how to login with the API and print the accounts name.



"""

import fuellock.lib.creditcard as creditcard
import fuellock.lib.account as account
import fuellock.lib.fuellock as fuellock
import fuellock.lib.giftcard as giftcard
import json

if __name__ == "__main__":
    # We need to save the login details into a variable. When you login there are 3 details that 7-Eleven responds
    # with. They are your device secret token, access token and your account id.
    # Device secret and access token are used for almost every request to
    # identify the user as you.
    myaccount = account.login("your@email.com", "password")

    # Get your account details. The response is a JSON array.
    get_account_details = json.loads(
        account.getAccountDetails(myaccount[0], myaccount[1])
    )
    # Print the users first name
    print(get_account_details["PersonalDetails"]["Name"]["Firstname"])

    account.logout(myaccount[0], myaccount[1])
