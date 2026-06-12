class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        return x / y
    
    def power(self, x, y):
        return x ** y
    
# Static Method Calls
print(Math.add(5, 3))        # Output: 8
print(Math.subtract(5, 3))   # Output: 2
print(Math.multiply(5, 3))   # Output: 15
print(Math.divide(5, 3))     # Output: 1.6666666666666667

# Usual Class Method
math = Math()
e = math.power(5, 3)          # Output: 125
print(e)
print(math.power(2, 4))      # Output: 16
