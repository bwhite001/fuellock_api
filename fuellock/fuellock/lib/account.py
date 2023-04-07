"""
    7-Eleven Python CLI



"""


class Account:
    def login(self, email, password):
        payload = (
            '{"Email":"'
            + email
            + '","Password":"'
            + password
            + '","DeviceName":"'
            + DEVICE_NAME
            + '","DeviceOsNameVersion":"'
            + ANDROID_VERSION
            + '"}'
        )
        tssa = generateTssa(BASE_URL + "account/login", "POST", payload)

        headers = {
            "User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)",
            "Connection": "Keep-Alive",
            "Host": "711-goodcall.lib.tigerspike.com",
            "Authorization": "%s" % tssa,
            "X-OsVersion": ANDROID_VERSION,
            "X-OsName": "Android",
            "X-DeviceID": DEVICE_ID,
            "X-AppVersion": APP_VERSION,
            "Content-Type": "application/json; charset=utf-8",
        }

        response = requests.post(
            BASE_URL + "account/login", data=payload, headers=headers
        )

        returnHeaders = response.headers
        returnContent = response.text

        returnContent = json.loads(returnContent)
        try:
            deviceSecret = returnContent["DeviceSecretToken"]
            accountID = returnContent["AccountId"]
            accountBalance = returnContent["DigitalCard"]["Balance"]

            accessToken = str(returnHeaders).split("'X-AccessToken': '")
            accessToken = accessToken[1].split("'")
            accessToken = accessToken[0]

            # These 3 variables are used for the basis of multiple requests, so it is a good idea to store them in
            # a variable when you call them (i.e. myaccount = account.login("email", "password"))
            #
            # deviceSecret and accessToken are used for every request where you need to be logged in.
            # accountID is used for locking in a fuel price.
            # accountBalance is useful to figure out how much fuel we can lock in
            self.deviceSecret
            self.accessToken
            self.accountID
            self.accountBalance
            return deviceSecret, accessToken, accountID, accountBalance
        except BaseException:
            # If the username and password is wrong, return the message
            return returnContent["Message"]

    def logout(self, deviceSecret, accessToken):
        payload = '""'
        tssa = generateTssa(BASE_URL + "account/logout", "POST", payload, accessToken)

        headers = {
            "User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)",
            "Connection": "Keep-Alive",
            "Host": "711-goodcall.lib.tigerspike.com",
            "Authorization": "%s" % tssa,
            "X-OsVersion": ANDROID_VERSION,
            "X-OsName": "Android",
            "X-DeviceID": DEVICE_ID,
            "X-AppVersion": APP_VERSION,
            "X-DeviceSecret": deviceSecret,
            "Content-Type": "application/json; charset=utf-8",
        }

        response = requests.post(
            BASE_URL + "account/logout", data=payload, headers=headers
        )

        return response.content

    def getAccountDetails(self, deviceSecret, accessToken):
        tssa = generateTssa(BASE_URL + "account/getaccountinfo", "GET", "", accessToken)

        headers = {
            "User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)",
            "Connection": "Keep-Alive",
            "Host": "711-goodcall.lib.tigerspike.com",
            "Authorization": "%s" % tssa,
            "X-OsVersion": ANDROID_VERSION,
            "X-OsName": "Android",
            "X-DeviceID": DEVICE_ID,
            "X-AppVersion": APP_VERSION,
            "X-DeviceSecret": deviceSecret,
        }

        response = requests.get(BASE_URL + "account/GetAccountInfo", headers=headers)

        return response.content

    def newPasswordRequest(self, deviceSecret, accessToken, password):
        payload = (
            '{"Password":"'
            + password
            + '","Token":"'
            + accessToken
            + '","DeviceName"'
            + DEVICE_NAME
            + '","DeviceOsNameVersion":"'
            + ANDROID_VERSION
            + '"}'
        )
        tssa = generateTssa(BASE_URL + "Account/NewPassword", "POST", payload)

        headers = {
            "User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)",
            "Connection": "Keep-Alive",
            "Host": "711-goodcall.lib.tigerspike.com",
            "Authorization": "%s" % tssa,
            "X-OsVersion": ANDROID_VERSION,
            "X-OsName": "Android",
            "X-DeviceID": DEVICE_ID,
            "X-AppVersion": APP_VERSION,
            "X-DeviceSecret": deviceSecret,
            "Content-Type": "application/json; charset=utf-8",
        }

        response = requests.post(
            BASE_URL + "Account/NewPassword", data=payload, headers=headers
        )

        return response.content

    def newAccountRegistration(
        self, dobTimestamp, email, firstName, password, phoneNumber, surname
    ):
        payload = (
            '{"DobSinceEpoch":"'
            + str(dobTimestamp)
            + '","EmailAddress":"'
            + email
            + '","FirstName":"'
            + firstName
            + '","OptInForPromotions":false,"OptInForSms":false,"Password":"'
            + password
            + '","PhoneNumber":"'
            + phoneNumber
            + '","Surname":"'
            + surname
            + '"}'
        )
        tssa = generateTssa(BASE_URL + "account/register", "POST", payload)

        headers = {
            "User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)",
            "Connection": "Keep-Alive",
            "Host": "711-goodcall.lib.tigerspike.com",
            "Authorization": "%s" % tssa,
            "X-OsVersion": ANDROID_VERSION,
            "X-OsName": "Android",
            "X-DeviceID": DEVICE_ID,
            "X-AppVersion": APP_VERSION,
            "Content-Type": "application/json; charset=utf-8",
        }

        response = requests.post(
            BASE_URL + "account/register", data=payload, headers=headers
        )

        return response.content

    def verifyAccount(self, VerificationCode):
        payload = (
            '{"VerificationCode":"'
            + VerificationCode
            + '","DeviceName":"'
            + DEVICE_NAME
            + '","DeviceOsNameVersion":"'
            + ANDROID_VERSION
            + '"}'
        )
        tssa = generateTssa(BASE_URL + "account/verify", "POST", payload)

        headers = {
            "User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)",
            "Connection": "Keep-Alive",
            "Host": "711-goodcall.lib.tigerspike.com",
            "Authorization": "%s" % tssa,
            "X-OsVersion": ANDROID_VERSION,
            "X-OsName": "Android",
            "X-DeviceID": DEVICE_ID,
            "X-AppVersion": APP_VERSION,
            "Content-Type": "application/json; charset=utf-8",
        }

        response = requests.post(
            BASE_URL + "account/verify", data=payload, headers=headers
        )

        return response.content
