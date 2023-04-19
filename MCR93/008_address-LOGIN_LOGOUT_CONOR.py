#log in / log out
#list of users and passwords required
#users = ["Conor", "Liam", "Shane", "John", "Zijnan")
#corresponding passwords = ["MCR93", "MCR94", "MCR95", "MCR96", "MCR97"]

users = [{"username": "Conor", "Password":"MCR93"},
        {"username": "Liam", "Password":"MCR94"},
        {"username": "Shane", "Password":"MCR95"},
        {"username": "John", "Password":"MCR96"},
        {"username": "Zijnan", "Password":"MCR97"}]

logged_in = False #user is logged out and has no access
logged_in_user = ""

Username = input("Please enter your username: ")
Password = input("Please enter your password: ")

for i in range(len(users)):

    if Username == users[i]["username"] and Password == users[i]["Password"]:
        print("Hello",Username,", you have logged in successfully!")
        logged_in = True #user is logged in and has access
        logged_in_user = Username

if logged_in == False:
    print("Invalid username or password")
