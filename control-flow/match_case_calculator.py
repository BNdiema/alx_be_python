
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        sum = num1 + num2
        print(f"The result is {sum}.")
    case "-":
        difference = num1 - num2
        print(f"The result is {difference}.")
    case "*":
        multiplication = num1 * num2
        print (f"The result is {multiplication}.")
    case "/":
        if num1 and num2 == 0:
            print("Cannot divide by zero.")
        else:
            division = num1 / num2
            print(f"The result is {division}.")
