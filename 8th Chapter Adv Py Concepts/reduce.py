from functools import reduce
a = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

c = reduce(add, a)
print(c)