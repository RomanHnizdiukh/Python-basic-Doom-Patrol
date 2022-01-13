while True:
    print("Welcome to calculator, please provide your operation with numbers: ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Operation: +, -, *, /")
    select = input("Select operations: ")

    if select == "+":
        print(num1, "+", num2, "=", num1 + num2)
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {select} {num2} = {num1 + num2} "))

    elif select == "-":
        print(num1, "-", num2, "=", num1 - num2)
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {select} {num2} = {num1 - num2} "))

    elif select == "*":
        print(num1, "*", num2, "=", num1 * num2)
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {select} {num2} = {num1 * num2} "))

    elif select == "/":
        print(num1, "/", num2, "=", num1 / num2)
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {select} {num2} = {num1 / num2} "))

    else:
        print("Invalid input")