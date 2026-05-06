# def fib :: Integer -> Integer
#     fib (0) = 0
#     fib (1) = 1
#     fib n = fib (n - 1) + fib (n - 2)

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(int(input("Enter a number to calculate its Fibonacci value: "))))