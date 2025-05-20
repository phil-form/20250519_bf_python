class Person:
    def __init__(self, lastname, firstname, birthdate):
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        
    def __str__(self):
        # return self.firstname + ' ' + self.lastname
        return f'{self.firstname};{self.lastname};{self.birthdate}'