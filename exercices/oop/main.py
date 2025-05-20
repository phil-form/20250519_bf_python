from Models.Account import Account
from Models.Person import Person
from datetime import datetime

pers = Person("Doe", "John", '1990-01-01')

acc = Account(1001, 1000, 250, pers)
