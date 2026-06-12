def divide(a,b): 
    try: 
        c = a/b
        return c

    except:
        print("An error occurred, You cannot divide by zero!")
        return None

    else:
        print("The division is ", c)

    finally:
        print("This will always be executed, whether an exception occurred or not.")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

result = divide(a,b)
print("Result of division: ", result)