

name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

#result = len(name)  # Get the length of the string
#result = name.find("A")  # Find the index of the first space
#result = name.rfind("a")  # Find the index of the last 'a'
#name = name.capitalize()  # Capitalize the first letter of the string
#name = name.upper()  # Convert the string to uppercase
#name = name.lower()  # Convert the string to lowercase 
result = name.isdigit()  # Check if the string contains only digits
result = name.isalpha()  # Check if the string contains only alphabetic characters
result = phone_number.count("-")  # Count occurrences of '-'
phone_number = phone_number.replace("-", " ")  # Replace '-' with space 
print(result)
print(phone_number)