class Employee:
    def __init__(self, _salary):
        self._salary = _salary
 
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        else:
            self._salary = value
    
emp = Employee(250000)

try:
    emp.salary = -5000
except ValueError as e:
    print("Error:", e)

print(emp.salary)
