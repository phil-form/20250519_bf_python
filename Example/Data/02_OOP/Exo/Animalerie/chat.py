from animal import Animal

class Chat(Animal):
    def __init__(self, nom, poids, taille, sexe, date_arrivee,
        poil_long, caractere, griffe_coupee) -> None:
        super().__init__(nom, poids, taille, sexe, date_arrivee, 0.5)
        self.__poil_long = poil_long
        self.__caractere = caractere
        self.__griffe_coupee = griffe_coupee

    @property
    def poil_long(self):
        return self.__poil_long

    @property
    def caractere(self):
        return self.__caractere

    @caractere.setter
    def caractere(self, value):
        self.__caractere = value

    @property
    def griffe_coupee(self):
        return self.__griffe_coupee

    @griffe_coupee.setter
    def griffe_coupee(self, value):
        self.__griffe_coupee = value 


    def crier(self):
        print("miaou")