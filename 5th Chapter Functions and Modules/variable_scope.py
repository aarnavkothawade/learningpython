z = 1# This is a variable in the global scope. It can be accessed from anywhere in the code.

def function1():
    print("This is function 1")
    print(z)  # Accessing the global variable 
    z = 10  # This creates a new local variable z that shadows the global variable
    print(z)  # This will print the local variable z

function1()