class Chat:
    def __init__(self, nom, poids, taille, sexe, 
        age, caractere, griffe_coupee, poil_long) -> None:
        self.__nom = nom
        self.__poids = poids
        self.__taille = taille
        self.__sexe = sexe
        self.__age = age
        self.__caractere = caractere
        self.__griffe_coupee = griffe_coupee
        self.__poil_long = poil_long

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    def crier(self):
        print("miaou")

c1 = Chat("lucky", 12, 40, True, 4, "farouche", False, False)

c1.crier()