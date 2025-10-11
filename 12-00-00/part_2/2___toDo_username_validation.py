

username=input("Enter your username: ")

if len(username)>12:
    print("Username must be less than 12 characters.")
elif username.find(" " )!=-1:
    print("Username must not contain spaces.")
elif  username.isdigit():
    print("Username must not be entirely numeric.")
else:
    print("Username is valid.")