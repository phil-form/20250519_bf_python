class MyFirstClass():

    # Constructor
    def __init__(self, name, age, admin=False) -> None:
        self.name = name
        self.age = age
        self.admin = admin

    # Destructor
    def __del__(self):
        print("destroy")

    def setAdmin(self):
        self.admin = not self.admin

    def isAdmin(self):
        return self.admin

    


p = MyFirstClass("Chris", 35)
print(p.name, p.age)

p.age = 24
p.name = "Jean"

print(p.name, p.age)

print(p.isAdmin())
p.setAdmin()
print(p.isAdmin())
