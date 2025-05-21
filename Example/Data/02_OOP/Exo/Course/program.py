from Models.Circuit import Circuit
from Models.Concurrent import Concurrent
from Models.Course import Course
from Models.Voiture import Voiture

spa = Circuit("Spa", 7004, 20)

c = Course("Technifutur", spa, 42)

v1 = Voiture("Audi", "R8", 81, 230)
v2 = Voiture("Audi", "R8", 80, 120)
v3 = Voiture("Audi", "R8", 80, 230)

riri = Concurrent("Riri", 1, v1)
fifi = Concurrent("Fifi", 1, v2)
Loulou = Concurrent("Loulou", 1, v3)

c.ajouter_participants(riri)
c.ajouter_participants(fifi)
c.ajouter_participants(Loulou)

c.demarrer_course()

winner = c.obtenir_vainqueur()

print(winner.se_decrire())