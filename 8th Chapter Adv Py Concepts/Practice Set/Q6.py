class NegativeNumberError(Exception):
        pass

try:
    a = int(input("Enter a number: "))

    if a < 0:
        raise NegativeNumberError("Number cannot be negative.")
    
    result = 45/a
    print(result)


except ValueError:
    print("The input is not a number.")
    
except ZeroDivisionError:
    print("Cannot divide by zero.")

except NegativeNumberError as e:
    print(e)
    