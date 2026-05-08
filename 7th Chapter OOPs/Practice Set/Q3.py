class Animal:
    def sound(self) :
        print("Some Sound")

class Dog(Animal) :
    def sound(self) :
        super().sound()
        print("Bark!")

d = Dog()
d.sound()