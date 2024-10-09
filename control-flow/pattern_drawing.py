positive_int = int(input("Enter the size of the pattern: "))
square = 0
while positive_int > square:
    for _ in range(positive_int):
        print("*", end="")
    print()
    square += 1
