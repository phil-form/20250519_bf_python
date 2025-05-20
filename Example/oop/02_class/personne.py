class Person:
    def __init__(self, nom, prenom, age = 42):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
p = Person("Nom", "Prénom")