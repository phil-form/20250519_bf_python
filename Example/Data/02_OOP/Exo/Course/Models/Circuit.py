class Circuit:
    def __init__(self, nom, longueur, max_voiture) -> None:
        self.__nom = nom
        self.__longueur = longueur
        self.__max_voiture = max_voiture

    @property
    def longueur(self):
        return self.__longueur