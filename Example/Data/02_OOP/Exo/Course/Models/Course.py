from Models.Circuit import Circuit
from Models.Concurrent import Concurrent

class Course:
    def __init__(self, nom, circuit, nb_tour) -> None:
        self.__nom = nom
        self.__circuit = circuit
        self.__nb_tour = nb_tour
        self.__concurrents = []

    def ajouter_participants(self, participant):
        if participant != None and isinstance(participant, Concurrent):
            self.__concurrents.append(participant)

    def demarrer_course(self):
        for i in range(self.__nb_tour):
            for concurent in self.__concurrents:
                concurent.realiser_tour(self.__circuit)

    def obtenir_vainqueur(self) -> Concurrent:
        winner = self.__concurrents[0]

        for concurent in self.__concurrents:
            if(concurent.temps_total < winner.temps_total):
                winner = concurent

        return winner

    