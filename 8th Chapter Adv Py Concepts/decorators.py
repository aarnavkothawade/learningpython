# Decorators
def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


# or you can call it as --> f = decorator(say_hello()) then call f() to execute the decorated function.