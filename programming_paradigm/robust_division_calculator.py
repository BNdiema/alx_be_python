def safe_divide(numerator, denominator):
    try:
        if int(numerator) and int(denominator) == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            result = int(numerator) / int(denominator)
            return f"The result of the division is {result}"
    except ValueError:
            return "Error: Please enter numeric values only."
