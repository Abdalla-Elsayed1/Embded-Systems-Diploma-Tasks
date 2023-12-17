user_data = {"Ahmed": "1394",
             "Amr": "9345",
             "Ali": "6078"}

user_name = input("Enter the username: ")
user_pass = input("Enter the password: ")

if user_name in user_data and user_pass == user_data[user_name]:
    print("Ya Welcome!")
else:
    print("Wrong credentials, please try again.")