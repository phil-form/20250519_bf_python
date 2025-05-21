#singleton
instance = []

class Cat:
    Paws = 4
    
    @staticmethod
    def staticMethod():
        instance.append("test")
        print("this method is static!")

Cat.staticMethod()

print(instance)