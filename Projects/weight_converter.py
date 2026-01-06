# Weight Converter

weight = float(input("Enter weight: "))
unit = input("Kilograms or pounds (K/L):   ")

if unit == "K":
    weight = weight * 2.205
    print(f"Converted weight: {weight}")
elif unit == "L":
    weight = weight / 2.205
    print(f"Converted weight: {weight}")
else:
    print("Invalid unit")

