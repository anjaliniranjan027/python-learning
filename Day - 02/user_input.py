# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name? ")
age = input("How old are you?")
print("HAPPY BIRTHDAY!")
age = int(age)  # Convert age from str to int so we can do math on it
age += 1
print(f"Hello {name}! ")
print(f"You are {age} years old.")