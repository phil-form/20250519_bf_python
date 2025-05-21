from Models.Circuit import Circuit

class Concurrent:
    def __init__(self, nom, numero, voiture) -> None:
        self.__nom = nom
        self.__numero = numero
        self.__voiture = voiture
        self.__temps = []

    @property
    def temps_total(self):
        return sum(self.__temps)

    def realiser_tour(self, circuit: Circuit):
        vit = self.__voiture.obtenir_vitesse() / 3.6
        distance = circuit.longueur

        temps = distance / vit

        self.__temps.append(temps)

    def se_decrire(self):
        return f"{self.__numero} {self.__nom} " + self.__voiture.se_decrire()