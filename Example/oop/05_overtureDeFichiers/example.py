from Models.Person import Person
import json
import csv

persons = []
with open('Datas/persons.json', 'r') as fd:
    data = json.load(fd)
    print(data)
    
    for val in data:
        persons.append(Person(val))
        
    for pers in persons:
        pers.lastname = 'Poiu'
    
# persData = {}
# persData['lastname'] = input("Entrer un nom : ")
# persData['firstname'] = input("Entrer un prénom : ")

# persons.append(Person(persData))

with open('Datas/persons.json', 'w') as fd:
    jsonText = str(persons)
    fd.write(jsonText)
    
with open('Datas/address.csv', 'r') as fd:
    reader = csv.DictReader(fd, fieldnames=["firstname", "lastname", "address", "number", "zip"], delimiter=';')
    
    for row in reader:
        print(row)
        
with open('Datas/address.csv', 'a') as fd:
    fd.write('\n')
    writer = csv.DictWriter(fd, fieldnames=["firstname", "lastname", "address", "number", "zip"], delimiter=';')
    writer.writerow({
        "firstname": "Test", 
        "lastname": "Test",
        "address": "Test asdf",
        "number": 12,
        "zip": 1234
    })