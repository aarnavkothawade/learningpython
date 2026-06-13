num = [1, 2, 3, 4, 5]

print(list(map(lambda x: x**3, num)))

num1 = [10, 11, 12, 13, 14]
print(list(filter(lambda x: x % 2 == 0, num1)))

from functools import reduce
a = [1, 2, 3, 4, 5]
c = reduce(lambda x, y: x * y, a)
print(c)