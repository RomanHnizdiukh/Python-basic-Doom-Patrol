while True:
    print("Welcome to calculator, please provide your operation with numbers: ")

    print("Operation: +, -, *, /")
    select = input("Select operations: ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

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
        try:
            print(num1, "/", num2, "=", num1 / num2)
        except ValueError:
            print("Please enter only numbers")
        except ZeroDivisionError:
            print("You can't divide by zero")
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {select} {num2} = {num1 / num2} "))

    else:
        print("Invalid input")