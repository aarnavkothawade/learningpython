# OOPs in Python - Object Oriented Programming System
# Class - Blueprint
class Employee:
    # Class Variable
    company = "Google"

    # Constructor # __init__ is a special method that is called when an object is instantiated
    def __init__(self, name, salary):
        self.name = name  # Instance Variable
        self.salary = salary  # Instance Variable

    # Method
    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

# Creating Objects
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Accessing Methods
emp1.show_details()
emp2.show_details()

# Modifying Class Variable
Employee.company = "Microsoft"
emp1.show_details()

emp2.name = "Charlie"  # Modifying Instance Variable
emp2.show_details()

