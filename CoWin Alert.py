import json
from datetime import datetime, timedelta
from GetData import getData
from FormMsg import formMsg
from GetPincode import getPincode

if __name__ == '__main__':

    t_date = datetime.today().strftime("%d%m%y")
    pin = getPincode()
    data = getData(pin,t_date)
    msg_body = formMsg(data)
    print(msg_body)

