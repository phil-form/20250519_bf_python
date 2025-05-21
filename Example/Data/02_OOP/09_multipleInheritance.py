class Animal:
    def __init__(self, name) -> None:
        self.name = name
    #region test
    def sleep(self):
        print("sleeping")

    def myFunc(self):
        print("From animal")
    #endregion

class Stomach:
    def __init__(self) -> None:
        self.isEmpty = True

    def eat(self):
        self.isEmpty = False

    def myFunc(self):
        print("From Stomach")

class Cat(Animal, Stomach):
    def __init__(self, name, color) -> None:
        super().__init__(name)
        Stomach().__init__()
        self.color = color

    def purr(self):
        print("purr purr purr")

    def myFunc(self):
        return super().myFunc()

    def myFunc2(self):
        return Stomach().myFunc()

class Car:
    pass

c = Cat("cat", "black")

print("Is c a child of Cat? ",isinstance(c, Cat))
print("Is c a child of Animal? ",isinstance(c, Animal))
print("Is c a child of Car? ",isinstance(c, Car))

c.myFunc()
c.myFunc2()
