# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in a key:value pair, and can be referred to by using the
# key name.
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:
y = thisdict.get("model")
print(y)
# You can change the value of a specific item by referring to its key name:
thisdict["year"] = 2018
print(thisdict)
# Loop through a dictionary
for x in thisdict:
    print(x)
# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])
# You can also use the values() function to return values of a dictionary:

for x in thisdict.values():
    print(x)
# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)
# Check if "model" is present in the dictionary:
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
# The len() function returns the number of items in the dictionary.

print(len(thisdict))
# Adding an item to the dictionary is done by using a new index key and assigning a value
thisdict["color"] = "red"
print(thisdict)
# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)
# The del keyword removes the item with the specified key name:
del thisdict["year"]
print(thisdict)
# The del keyword can also delete the dictionary completely:
del thisdict
# print(thisdict) # this will cause an error because the dictionary no longer exists
# The clear() method empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}   
thisdict.clear()
print(thisdict)
