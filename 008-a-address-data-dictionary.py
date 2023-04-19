# LOGIN  / LOGOUT - Conor
users = [
    {"username": "A Username", "password": "A Password"},
    {"username": "Conor", "password": "mcr93"}
    ]


# Login Status
logged_in = True    # A user is logged in and address data can be accessed
logged_in = False   # A user is logged out and address data can not be accessed


# Address Listing
addrs = [
    {"f_name": "A first name",
     "l_name": "A last/family name",
     "street": "A road/street name",
     "number": "A house number",
     "eircode": "Eircode/ZIP/Postal code",
     "phone": "Phone Number"},
    {"f_name": "Seamus",
     "l_name": "Kavanagh",
     "street": "O'Connel Street Upper",
     "number": "11-13",
     "eircode": "D01 F9C1",
     "phone": "01 - 666 1122"}
    ]


# Looping example for the address list
for i in range(len(addrs)):
    print(addrs[i]['f_name'])

