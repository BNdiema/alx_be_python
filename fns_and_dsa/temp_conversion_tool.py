FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def convert_temp():
    temp = float(input("Enter the temperature to convert: "))
    temp_to_convert = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if temp_to_convert == "F":
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    elif temp_to_convert == "C":
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")