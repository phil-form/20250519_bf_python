#singleton
instance = []

class Cat:
    @staticmethod
    def staticMethod():
        instance.append("test")
        print("this method is static!")

def printInstance():
    print(instance)