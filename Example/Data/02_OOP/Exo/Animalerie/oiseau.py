from animal import Animal

class Chien(Animal):
    def __init__(self, nom, poids, taille, sexe, date_arrivee,
        habitat, couleur) -> None:
        super().__init__(nom, poids, taille, sexe, date_arrivee, 1.0)
        self.__couleur = couleur
        self.__habitat = habitat

    def crier(self):
        print("piou piou")