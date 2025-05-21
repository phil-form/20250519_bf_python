class User(dict):
    def __init__(self) -> None:
        self.username = "test"
        self.password = "superSecureP@s5w0rD!"

    def printName(self):
        print(self.__class__.__name__)

    # return a string representation
    def __repr__(self) -> str:
        return self.username + " " + self.password
    
    # return a string is called by default by print()
    def __str__(self) -> str:
        return str("Username : " + self.username + " password : " + self.password)

    # is called when use ==
    def __eq__(self, o: object) -> bool:
        return isinstance(o, User) and self.username == o.username and self.password == o.password

    #by default __ne__ return the opposite of __eq__
    def __ne__(self, o: object) -> bool:
        return self.username != o.username or self.password != o.password

    def __lt__(self, other) -> bool:
        return len(self.username) < len(other.username)

    def __le__(self, other) -> bool:
        return len(self.username) <= len(other.username)

    def __gt__(self, other) -> bool:
        return len(self.username) > len(other.username)

    def __ge__(self, other) -> bool:
        return len(self.username) >= len(other.username)


user = User()
user.printName()
print(user.__class__.__name__)
print(user.__class__.__base__)
print(user.__dict__)
print(user.__repr__())
print(user)
user2 = User()
print(user == user2)
user2.password = "1234567"
print(user == user2)
user.username = "te"
print(user < user2)
user.username = "teasa"
print(user <= user2)