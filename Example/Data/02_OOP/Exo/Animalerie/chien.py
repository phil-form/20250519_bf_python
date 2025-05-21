from animal import Animal

class Chien(Animal):
    def __init__(self, nom, poids, taille, sexe, date_arrivee,
        couleur_colier, dresser, race) -> None:
        super().__init__(nom, poids, taille, sexe, date_arrivee, 1.0)
        self.__couleur_colier = couleur_colier
        self.__dresser = dresser
        self.__race = race

    def crier(self):
        print("wouf")