class Employee: 
    salary = 20000  # Class attribute
    def __init__(self, name, bond, salary): 
        self.name = name 
        self.bond = bond
        self.salary = salary 

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Name: {self.name}, Bond: {self.bond}, Salary: {self.salary}")

employee1 = Employee("John Doe", 3, 50000)
employee1.get_info()

# Object Introspection 
print(employee1.__dict__)  # Shows the attributes of the object
print(dir(employee1))  # Shows the methods and attributes of the object
print(Employee.salary)  # Accessing class attribute
print(employee1.get_salary())  # Accessing instance method to get salary