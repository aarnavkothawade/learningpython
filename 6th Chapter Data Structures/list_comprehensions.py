# List Comptehensions
# List comprehensions are a concise way to create lists in Python. They consist of brackets containing an expression followed by a for clause, and optionally, one or more if clauses.


squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# You can also include an if clause to filter items from the original list. For example, to create a list of even squares:

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# List comprehensions can also be used to create lists of tuples. For example, to create a list of (x, x^2) pairs:
squares_pairs = [(x, x**2) for x in range(10)]
print(squares_pairs)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]

# List comprehensions can also be nested. For example, to create a list of all possible pairs of numbers from two lists:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c'] 
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)  # Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

