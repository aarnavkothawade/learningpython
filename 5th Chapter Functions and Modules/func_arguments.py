def add(a, b): # Parameters
    return a + b

sum = add(b=134, a=3) # Arguments
print(sum)  # Output: 137 


# Default arguments can be overwritten when function is called with the position of the parameter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!