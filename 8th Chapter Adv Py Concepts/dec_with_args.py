def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name): # You need to pass the argument 'name' when calling the function compulsorily .
    print(f"Hello, {name}!")

greet(input("Enter your name: ").strip())