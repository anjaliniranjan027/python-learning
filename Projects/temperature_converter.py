# Temperature Converter
# This program converts temperatures between Celsius and Fahrenheit.

unit = input("Celsius or Fahrenheit (C/F):   ")
temperature = float(input("Enter temperature: "))  

if unit == "C":
    temperature = (temperature * 9/5) + 32
    print(f"Converted temperature: {temperature} F")        
elif unit == "F":
    temperature = (temperature - 32) * 5/9
    print(f"Converted temperature: {temperature} C")            
else:
    print("Invalid unit")
