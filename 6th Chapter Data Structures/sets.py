# Sets

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Sets are unordered, so you cannot access items by index
# You can loop through the set
for fruit in fruits:
    print(fruit)
# You can check if an item is in the set
print("banana" in fruits)

# You can add items to a set
fruits.add("orange")
print(fruits)

# You can remove items from a set
fruits.remove("banana")
print(fruits)

# You can also use the discard method to remove an item, but it won't raise an error if the item is not found
fruits.discard("banana")
print(fruits)

# You can clear all items from a set
fruits.clear()
print(fruits)

# You can create a set from a list
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set)

# You can perform set operations like union, intersection, and difference
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))  # {1, 2, 3, 4, 5}
print(set_a.intersection(set_b))  # {3}
print(set_a.difference(set_b))  # {1, 2}
