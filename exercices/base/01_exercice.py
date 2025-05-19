# Exercice 1
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prenom : ")
print("Bienvenue", nom, prenom)

# Année bisextile :
annee = int(input("Entrez une année : "))

if(annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0):
    print("Bisextile")
else:
    print("Non bisextile")