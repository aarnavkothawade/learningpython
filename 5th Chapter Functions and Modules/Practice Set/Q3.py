def full_name(first, last):
    full_name = first + " " + last
    return full_name.title()

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
formatted_name = full_name(first_name, last_name)
print("Your full name is: " + formatted_name)