username = input("Enter your username: ")

if username.strip() == "":
    print("Invalid username: Username must not contain only spaces.")

elif len(username) < 5:
    print("Invalid username: Username must contain at least 5 characters.")

elif username.lower() == "admin":
    print("Invalid username: Username must not be 'admin'.")

else:
    print("Valid username.")
