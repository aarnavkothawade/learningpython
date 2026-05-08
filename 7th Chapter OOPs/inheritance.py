# Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

my_car = Car("Toyota", "Corolla", 4)
my_car.display_info()
my_car1 = Vehicle("Honda", "Civic")
my_car1.display_info()