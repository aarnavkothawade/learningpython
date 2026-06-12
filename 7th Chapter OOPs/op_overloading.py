# Operator Overloading in Python allows you to define the behavior of operators for custom classes. This means you can use operators like +, -, *, /, etc., with instances of your classes, and they will behave according to the rules you define.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: Vector(6, 8)     # v = v1.__add__(v2) will give out the same result as v1 + v2
print(v1 - v2)  # Output: Vector(-2, -2)   # v = v1.__sub__(v2) will give out the same result as v1 - v2
print(v1 * 2)   # Output: Vector(4, 6)     # v = v1.__mul__(2) will give out the same result as v1 * 2
print(v1 / 2)   # Output: Vector(1.0, 1.5) # v = v1.__truediv__(2) will give out the same result as v1 / 2
