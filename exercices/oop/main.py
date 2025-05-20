from Models.Courant import Courant
from Models.Person import Person
from datetime import datetime

pers = Person("Doe", "John", '1990-01-01')
print(pers)

acc = Courant(1001, 1000, pers, 250)
print(acc)

acc.retrait(1100)
print(acc.amount)
acc.retrait(800)
print(acc.amount)
