try:
    num1 = int(float(input("Enter the first number: ")))
    operator = input("Enter the operator: ")
    num2 = int(float(input("Enter the second number: ")))
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Invalid operator.")
except ValueError:
    print("Invalid value.")
except ZeroDivisionError:
    print("Can't divide by zero.")
