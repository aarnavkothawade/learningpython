# Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

t = ("apple", "banana", "cherry")
print(t)

# Tuples are unchangeable, meaning that you cannot change, add, or remove items after the tuple has been created.
# But you can delete the tuple completely:
t = ("apple", "banana", "cherry")
del t

# Tuple Length
t = ("apple", "banana", "cherry")
print(len(t))

# Create Tuple With One Item
t = ("apple",)
print(t)

# NOT a tuple
t = ("apple")
print(t)

# Tuple Items - Data Types
t = ("apple", 1, True)
print(t)
