text = input("Enter a string to check if it is a palindrome: ")
t = text[::-1].lower()
print(t)
if text.lower() == t:
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")