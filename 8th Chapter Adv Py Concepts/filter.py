def is_greater_than_10(x):
    if x > 10: 
        return True
    else:
        return False
    
numbers = [5, 10, 15, 20, 25]

new = list(filter(is_greater_than_10, numbers))
print(new)

#Using a lambda function instead of defining a separate function
new_lambda = list(filter(lambda x: x > 10, numbers))
print(new_lambda)
