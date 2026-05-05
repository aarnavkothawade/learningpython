a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

c = input("Enter the operator (+, -, *, /): ")

match c :
    case "+":
        print(f"The sum of {a} and {b} is: {a + b}")
    case "-":
        print(f"The difference of {a} and {b} is: {a - b}")
    case "*":
        print(f"The product of {a} and {b} is: {a * b}")
    case "/":
        if b != 0:
            print(f"The quotient of {a} and {b} is: {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator. Please enter one of the following: +, -, *, /.")  