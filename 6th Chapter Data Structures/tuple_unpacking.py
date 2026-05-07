# Tuple Unpacking
# Tuple unpacking is a powerful feature in Python that allows you to assign values from a tuple (or any iterable) to multiple variables in a single line of code. This can make your code more concise and easier to read.
# Basic Tuple Unpacking
# You can unpack a tuple into individual variables like this:
# Example 1: Basic Tuple Unpacking
point = (10, 20)
x, y = point
print(f"x: {x}, y: {y}")  # Output: x: 10, y: 20
# In this example, the values from the tuple `point` are unpacked into the variables
# `x` and `y`.
# Unpacking with More Variables
# If the tuple has more values than the number of variables you want to unpack, you can
# use the `*` operator to capture the remaining values in a list.
# Example 2: Unpacking with More Variables
data = (1, 2, 3, 4, 5)
a, b, *rest = data
print(f"a: {a}, b: {b}, rest: {rest}")  
# Output: a: 1, b: 2, rest: [3, 4, 5]
# In this example, `a` and `b` capture the first two values of the tuple, while `rest`
# captures the remaining values in a list.
# Unpacking with Fewer Variables
# If the tuple has fewer values than the number of variables you want to unpack, you can
# use the `*` operator to capture the missing values as an empty list.
# Example 3: Unpacking with Fewer Variables
data = (1, 2)
a, b, *rest = data
print(f"a: {a}, b: {b}, rest: {rest}")  # Output: a: 1, b: 2, rest: []
# In this example, `a` and `b` capture the values of the tuple, while `rest` captures
# the missing values as an empty list.
# Unpacking in Loops
# You can also use tuple unpacking in loops to iterate over tuples of values.
# Example 4: Unpacking in Loops
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"x: {x}, y: {y}")
# Output:
# x: 1, y: 2
# x: 3, y: 4
# x: 5, y: 6

