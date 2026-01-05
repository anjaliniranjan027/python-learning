# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter you age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")        
else:
    print("You must me 18+ to sign up")