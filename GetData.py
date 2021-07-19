import requests

def getData(pin,date):
    data = []
    for p in pin:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(p,
                                                                                                                     date)
        result = requests.get(URL)
        json_result = result.json()
        temp2 = []
        for center in json_result["centers"]:
            temp = {}
            ses = []
            vac = []
            for session in center["sessions"]:
                ses.append({'date': session["date"],
                            'available_capacity': session["available_capacity"],
                            'min_age_limit': session["min_age_limit"],
                            'slots': session["slots"]})
            if "vaccine_fees" in center:
                for vaccines in center["vaccine_fees"]:
                    vac.append({'vaccine': vaccines["vaccine"],
                                'fee': vaccines["fee"]})

            temp['name'] = center["name"]
            temp['address'] = center["address"]
            temp['pincode'] = center["pincode"]
            temp['from'] = center["from"]
            temp['to'] = center["to"]
            temp['fee_type'] = center["fee_type"]
            temp['vaccine'] = vac
            temp['sessions'] = ses

            temp2.append(temp)
        data.append(temp2)
    return data
