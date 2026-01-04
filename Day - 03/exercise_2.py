# Exercise 2: Calculate Area of Circle

import math

radius = float(input("Enter radius of the circle : "))
area = math.pi * pow(radius, 2)
print(f"Area of circle is : {area}")
print(f"Rounded Area of circle is : {round(area, 2)}cm²")