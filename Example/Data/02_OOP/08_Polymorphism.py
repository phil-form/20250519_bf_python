class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def sleep(self):
        print("sleeping")

class Cat(Animal):
    def __init__(self, name, color) -> None:
        super().__init__(name)
        self.color = color

    def purr(self):
        print("purr purr purr")

class Car:
    pass

c = Cat("cat", "black")

print("Is c a child of Cat? ",isinstance(c, Cat))
print("Is c a child of Animal? ",isinstance(c, Animal))
print("Is c a child of Car? ",isinstance(c, Car))

