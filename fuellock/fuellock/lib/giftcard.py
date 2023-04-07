"""
    7-Eleven Python CLI



"""


class GiftCard:
    def getDigitalCardBalance(deviceSecret, accessToken):
        tssa = generateTssa(BASE_URL + "GiftCard/Balance", "GET", "", accessToken)

        headers = {
            "User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)",
            "Connection": "Keep-Alive",
            "Host": "711-goodcall.lib.tigerspike.com",
            "Authorization": "%s" % tssa,
            "X-OsVersion": ANDROID_VERSION,
            "X-OsName": "Android",
            "X-DeviceID": DEVICE_ID,
            "X-AppVersion": "1.7.0.2009",
            "X-DeviceSecret": deviceSecret,
        }

        response = requests.get(BASE_URL + "GiftCard/Balance", headers=headers)

        return response.content

    def getPhysicalCardBalance(deviceSecret, accessToken, GiftCardNumber, GiftCardPin):
        payload = (
            '{"GiftCardNumber":'
            + GiftCardNumber
            + ',"GiftCardPin":"'
            + GiftCardPin
            + '"}'
        )
        tssa = generateTssa(
            BASE_URL + "GiftCard/PhysicalBalance", "POST", payload, accessToken
        )

        headers = {
            "User-Agent": "Apache-HttpClient/UNAVAILABLE (java 1.4)",
            "Connection": "Keep-Alive",
            "Host": "711-goodcall.lib.tigerspike.com",
            "Authorization": "%s" % tssa,
            "X-OsVersion": ANDROID_VERSION,
            "X-OsName": "Android",
            "X-DeviceID": DEVICE_ID,
            "X-AppVersion": "1.7.0.2009",
            "X-DeviceSecret": deviceSecret,
            "Content-Type": "application/json; charset=utf-8",
        }

        response = requests.get(BASE_URL + "GiftCard/PhysicalBalance", headers=headers)

        return response.content
