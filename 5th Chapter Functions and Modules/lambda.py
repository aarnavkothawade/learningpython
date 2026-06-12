# lambda functions in python are anonymous functions that can have any number of arguments but only one expression. They are defined using the lambda keyword.


square = lambda x: x ** 2

noraisedtono = lambda x: x ** x

print(square(int(input("Enter a number whose square is to be calculated: "))))

print(noraisedtono(int(input("Enter a number whose raised to itself is to be calculated: "))))