# Exercise 1: Calculate the circumference of a circle given its radius.
import math

radius = float(input("Enter the radius of the circle: "))
# C= 2πr

circumference = 2 * math.pi * radius
print(f"Circumference of the circle is : {circumference} ")
print(f"Rounded Circumference of the circle is : {round(circumference, 2)}cm")

