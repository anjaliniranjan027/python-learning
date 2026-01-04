# Exercise 3: Calculate Length of Hypotenuse

import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

# c = a² + b²
c = math.sqrt(pow(a, 2)+ pow(b, 2))
print(f"The length of hypotenuse is : {c}")
print(f"Rounded length of hypotenuse is : {round(c, 2)}")   