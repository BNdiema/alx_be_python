fahrenheit_to_celsius_factor = 5/9
celsius_to_fahrenheit_factor = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * fahrenheit_to_celsius_factor

def convert_to_fahrenheit(celsius):
    return (celsius * convert_to_celsius) + 32

def convert_temp():
    temp = float(input("Enter the temperature to convert: "))
    temp_to_convert = input("Is this temperature in Celsius of Fahrenheit? (C/F): ").strip().upper()
    if temp_to_convert == "F":
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    elif temp_to_convert == "C":
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    else:
        print("Invalid temperature")