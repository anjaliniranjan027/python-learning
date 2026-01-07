# conditional expressions = A one-line shorthand for if-else statements
#                           aka ternary operators   
#                           Print or assign one or two values based on a condition
#                           x if condition else y

# example 1
num = 5

print("positive" if num > 0 else "negative")

# example 2
num = 6

print("even" if num % 2 == 0 else "odd")

# example 3
a = 6
b = 7

max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

# example 4
user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)