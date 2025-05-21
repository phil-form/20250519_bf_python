import numpy as np

example = np.array([[1, 2, 3,], [4, 5, 6], [7, 8, 9]])
print(example)

# accéder à un élément
print(example[0, 0])
print(example[0, 1])
print(example[1, 0])

# petit rappel du slicing dans un tableau python
tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tab[3:])
print(tab[:3])
print(tab[3:6])

# récupérer la première colonne
print(example[:, 0])

# récupérer la première ligne
print(example[0, :])

# récupérer de l'index 1 à la fin de la colonne et la même chose pour la ligne
print(example[1:, 1:])

# Subsetting
example[1:, 1:] = 10
print(example)

D = np.random.randint(0, 10, (5, 5))
print(D)
print(D < 5)
print(D[D < 5])

# Copier un tableau
E = D.copy()
# Ici on doit utiliser les bitwise operator
# ou = |
# et = & 
# not = ~
# xor = ^
E[(E < 4) | (E == 9)] = 4
print(E)