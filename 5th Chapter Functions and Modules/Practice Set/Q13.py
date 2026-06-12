def safe_divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b
    
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: Error: Division by zero is not allowed.