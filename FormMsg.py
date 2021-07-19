def formMsg(data):

    if not data:
        msg = "No Slots available for the given parameters"
        return msg
    else:
        msg = "Here the the Slots which are currently available.\n"

    count = 0
    for pin in data:
        msg += "PINCODE -> " + str(pin[0]['pincode']) + "\n"
        for center in pin:
            count+=1
            msg += str(count) + "\n" + "Name : " + center['name'] + "\n"
            msg += "Address : " + center['address'] + "\n"
            msg += "Slots from - " + center['from'] + "-" + center['to'] + "\n"
            msg += "Fee : " + center['fee_type'] + "\n"

            if len(center['vaccine']) > 0:
                for vac in center['vaccine']:
                    msg += "Type - " + vac['vaccine'] + " fee - ₹" + vac['fee'] + "\n"

            if len(center['sessions']) > 0:
                msg += "Slots" + "\n"
                for ses in center['sessions']:
                    msg += "Date - " + ses['date'] + " Availability - " + str(ses['available_capacity']) + "\n"

                    if len(ses['slots']) > 0:
                        for slot in ses['slots']:
                            msg += slot + "\n"

                msg += "\n"

            msg += "\n\n"

    return msg




