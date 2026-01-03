# Typscasting = the process of converting a variable from one data type to another

name = "John"
age = 30
gpa = 3.5
is_student = True   

gpa = int(gpa)  # Convert float to int
print(gpa)

age = float(age)  # Convert int to float
print(age)

age = str(age)  
print(age)  # Convert int to str
print(type(age))

age += 1  # This will cause an error since age is now a string
print(age)

name = bool(name)  # Convert str to bool
print(name)
