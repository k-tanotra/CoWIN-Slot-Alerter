import re
def check(a):
    matched = re.match("^[1-9][0-9]{5}$", a)
    return bool(matched)

def getPincode():
    pincode = []
    print("Enter the Pincodes.")
    while(True):
        a = input()
        if a == "":
            break
        if check(a):
            pincode.append(a)
        else:
            print("enter a valid Pincode")
    return pincode