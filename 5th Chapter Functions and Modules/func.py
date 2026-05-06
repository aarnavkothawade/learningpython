# Functions in Python are defined using the `def` keyword, followed by the function name and parentheses. The code block within every function starts with a colon (:) and is indented.

def display() :
    print("Hello World")

# To call a function, use the function name followed by parentheses.
display()  # Output: Hello World



# Functions can also take parameters, which are values you can pass to the function to customize its behavior.  
def greet(name) :
    print("Hello, " + name + "!")

greet(input("Enter your name: ").title())  # Output: Hello, Alice!


def add(a, b) :
    return a+b


o1 = add(5,3)
print(o1)