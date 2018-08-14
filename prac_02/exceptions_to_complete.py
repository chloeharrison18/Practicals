finished = False
result = 0
while not finished:
    try:
        value_1 = int(input("Enter first integer: "))
        value_2 = int(input("Enter second integer: "))
        result = value_1 / value_2
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)