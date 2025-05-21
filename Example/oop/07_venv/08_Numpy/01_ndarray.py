# importer numpy pour pouvoir l'utiliser
import numpy as np

# Création d'un table à une dimension
arr = np.array([1, 2, 3])
print(arr)

# afficher la forme du tableau (nombre de dimension et lignes)
print(arr.shape)

# Connaitre le nombre de dimensions 
print(arr.ndim)

# Crée un tableau à plusieurs dimensions remplis de 0 (lignes/colonnes)
zeros = np.zeros((3,3))
print(zeros)

arr2 = np.ones((4,4))
print(arr2)

eye = np.eye(4)
print(eye)

# création d'un tableau avec des données aléatoires
random_values = np.random.randn(4, 4)
print(random_values)

# Crée un tableau d'un espace linéaire 
lin = np.linspace(0, 10, 5)
print(lin)

# Transmations 
# concatener des tableaux horizontalement
c = np.hstack((arr2, eye))
print(c)

# concatener des tableaux verticalement
c = np.vstack((arr2, eye))
print(c)

#
print(c.shape)
d = c.reshape((4,8))
print(d)