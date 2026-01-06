# logical operators = evaluate multiple conditions (or, and, not)
#                      or = at least one condition must be true
#                      and = all conditions must be true
#                      not = inverts true/false value

# example 1 - or
temp = 22
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Stay inside")   
else:
    print("Go outside") 

# example 2 - and
temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print("Go to the beach")
else:
    print("Go to the park")

# example 3 - not
is_weekend = False

if not is_weekend:
    print("Go to work")    
else:
    print("Sleep in")