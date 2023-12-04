usernames =["Ahmed","Amr","Ali"]
passwords=["1394","9345","6078"]

user_data=list(zip(usernames,passwords))
    
user_input=(input("enter user name: "),input("enter user password: "))

if user_input in user_data:
    print("ya welcome")
else:
    print("incorrect entry")