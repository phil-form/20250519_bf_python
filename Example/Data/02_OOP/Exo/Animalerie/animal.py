from abc import ABC, abstractmethod
import datetime

class Animal(ABC):
    def __init__(self, nom, poids, taille, sexe, date_arrivee,
        proba_deces) -> None:
        self.__nom = nom
        self.__poids = poids
        self.__taille = taille
        self.__sexe = sexe
        self.__date_arrivee = date_arrivee
        self.__proba_deces = proba_deces

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def poids(self):
        return self.__poids

    @nom.setter
    def poids(self, value):
        self.__poids = value

    @abstractmethod
    def crier(self):
        pass