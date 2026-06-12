# Strings are IMMUTABLE in Python, which means that once a string is created, it cannot be changed. However, Python provides a variety of string methods that allow you to manipulate and work with strings effectively. Here are some common string methods:

name = "Aarnav"
length = len(name)

print(length)

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

print(name.strip())  # Removes leading and trailing whitespace
print(name.lstrip())  # Removes leading whitespace
print(name.rstrip())  # Removes trailing whitespace

print(name.replace("a", "o"))  # Replaces all occurrences of 'a'
print(name.split("a"))  # Splits the string into a list based on the delimiter 'a'
print(name.join(["Hello", "World"]))  # Joins the elements of the list with the string as a separator

print(name.find("n"))  # Returns the index of the first occurrence of 'n'
print(name.count("a"))  # Counts the number of occurrences of 'a'

print(name.startswith("Aa"))  # Checks if the string starts with "Aa"
print(name.endswith("av"))  # Checks if the string ends with "av"
print(name.isalpha())  # Checks if all characters in the string are alphabetic
print(name.isdigit())  # Checks if all characters in the string are digits
print(name.isalnum())  # Checks if all characters in the string are alphanumeric

print(name.center(20, "*"))  # Centers the string within a field of a specified width, padded with a specified character
print(name.ljust(20, "-"))  # Left-justifies the string within a field of a specified width, padded with a specified character
print(name.rjust(20, "-"))  # Right-justifies the string within a field of a specified width, padded with a specified character

print(name.zfill(20))  # Pads the string with zeros on the left, to fill a specified width


text = "Apples, Bananas, Cherries"
print(text.split(", "))  # Splits the string into a list based on the delimiter ", "

l = ["Apples", "Bananas", "Cherries"]
print(", ".join(l))  # Joins the elements of the list into a single string, separated by ", "

