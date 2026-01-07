# Validate user input exercise


username = input("Enter your username: ")

if len(username) > 12:  
    print("Username too long")
elif not username.find(" ") == -1:  
    print("Username should not contain spaces")
elif not username.isalpha():    
    print("Username should only contain alphabetic characters")
else:
    print(f"Welcome {username}")