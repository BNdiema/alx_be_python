number = int(input("Enter a number to see its multiplication table: "))
for digit in range(1, 10 + 1):
    result = digit * number
    print(f"{number} * {digit} = {result} ")
