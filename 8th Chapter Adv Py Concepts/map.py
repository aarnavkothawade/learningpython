#Map helps applying the same function to all the elements of a list, and collecting the results in a new list. 

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x * x

squared_numbers = list(map(square, numbers))  # you need to convert the map object to a list to see the results
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


#You can also use a lambda function instead of defining a separate function.
squared_numbers_lambda = list(map(lambda x: x * x, numbers))
print(squared_numbers_lambda)  # Output: [1, 4, 9, 16, 25]

#Map can also be used with multiple iterables. The function will be applied to the elements of the iterables in parallel.
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

def add(x, y):
    return x + y

added_numbers = list(map(add, numbers1, numbers2))
print(added_numbers)  # Output: [5, 7, 9]


#Using a lambda function for the same operation
added_numbers_lambda = list(map(lambda x, y: x + y, numbers1, numbers2))
print(added_numbers_lambda)  # Output: [5, 7, 9]
