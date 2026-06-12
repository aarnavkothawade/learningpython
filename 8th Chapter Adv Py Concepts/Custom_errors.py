while True: 
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(a/b)

    except ZeroDivisionError:
        raise ValueError("You can't divide by zero!")
        print("You can't divide by zero!")

    except ValueError:
        print("Invalid input! Please enter a valid number. You tried to type cast a string to an integer.")

    
    except Exception as e : 
        print("Enter a Number only! ", e )

