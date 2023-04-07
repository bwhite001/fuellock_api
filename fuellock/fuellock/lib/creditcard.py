"""
    7-Eleven Python CLI

"""


class CreditCard:
    def getCreditCards(deviceSecret, accessToken):
        tssa = generateTssa(BASE_URL + "CreditCard/List", "GET", "", accessToken)

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

        response = requests.get(BASE_URL + "CreditCard/List", headers=headers)

        returnContent = json.loads(response.content)

        ccID = returnContent[0]["Id"]
        MaskPan = returnContent[0]["MaskPan"]

        return ccID, MaskPan

    def beginCCTransaction(creditcardId, amount, deviceSecret, accessToken):
        payload = '{"CreditCardId":"' + creditcardId + '","Amount":"' + amount + '"}'
        tssa = generateTssa(
            BASE_URL + "GiftCard/StartTopUp2", "POST", payload, accessToken
        )

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
            BASE_URL + "GiftCard/StartTopUp2", data=payload, headers=headers
        )

        returnContent = json.loads(response.content)

        TraceId = returnContent["TraceId"]
        PayUrl = returnContent["PayUrl"]

        return TraceId, PayUrl

    def verifyCcTransaction(cvv, traceId, payurl, deviceSecret, accessToken):
        payload = (
            '{"ccv":"'
            + str(cvv)
            + '","traceId":"'
            + traceId
            + '","requestOrigin":"MOBILE"}'
        )

        tssa = generateTssa(payurl, "POST", payload, accessToken)

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

        response = requests.post(payurl, data=payload, headers=headers)

        return response.content

    def confirmCreditCardTransaction(TraceId, MaskedPan, deviceSecret, accessToken):
        payload = '{"TraceId":"' + TraceId + '","MaskedPan":"' + MaskedPan + '"}'
        tssa = generateTssa(
            BASE_URL + "GiftCard/ConfirmTopUp", "POST", payload, accessToken
        )

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
            BASE_URL + "GiftCard/ConfirmTopUp", data=payload, headers=headers
        )

        return response.content
