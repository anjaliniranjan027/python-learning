# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?  ")
price = float(input("What is the price? "))
quantity = int(input("How many do you want to buy? "))
total = price*quantity

print(f"You have bought {quantity} x {item}(s)")
print(f"Total price is: Rs.{total}")  

              