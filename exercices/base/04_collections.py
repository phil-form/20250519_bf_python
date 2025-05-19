# !! initialiser la liste !
tab = []

for i in range(6):
    nbr = int(input("Entrez un nombre : "))
    tab.append(nbr)
    
for val in tab:
    print(val)
    
length = len(tab)

for i in range(length):
    print(tab[i])
    
# Exercice 2 -> liste des exposants de 2^1 à 2^10
# soit je nettoie le tableau
tab.clear()

# soit je crée un nouveau tableau
tab = []

for i in range(10):
    tab.append(2 ** (i + 1))
    
print(tab)