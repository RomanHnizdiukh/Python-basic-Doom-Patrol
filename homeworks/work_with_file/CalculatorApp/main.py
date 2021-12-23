while True:
    print("Welcome to calculator, please provide your operation with numbers: ")

    num1 = int(input(" Enter the first number: "))
    operator = input(" Enter operator:")
    num2 = int(input(" Enter the second number: "))
    result = num1 + num2
    result2 = num1 - num2

    if operator == "+":
        print(f"{num1} {operator} {num2} = {result}")
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {operator} {num2} = {result} "))
    elif operator == "-":
        print(f"{num1} {operator} {num2} = {result2}")
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {operator} {num2} = {result2} "))
    else:
        print("Invalid input, please provide operator: '+' or '-'")
