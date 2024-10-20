def safe_divide(numerator, denominator):
    try:
        if float(numerator) and float(denominator) == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            result = float(numerator) / float(denominator)
            return f"The result of the division is {result}"
    except ValueError:
            return "Error: Please enter numeric values only."
