import random

class Voiture:
    def __init__(self, marque, model, vit_min, vit_max) -> None:
        self.__marque = marque
        self.__model = model
        self.__vit_min = vit_min
        self.__vit_max = vit_max

    def obtenir_vitesse(self):
        return random.randint(self.__vit_min, self.__vit_max)

    def se_decrire(self) -> str:
        return f"{self.__marque} {self.__model}"