
def perform_operation(num1, num2, operation):

    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num1 and num2 == 0:
                return "Cannot divide by zero"
            elif operation:
                return num1 / num2
