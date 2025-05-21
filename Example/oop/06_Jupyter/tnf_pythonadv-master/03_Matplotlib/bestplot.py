import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target

plt.figure(figsize=(12,12))
ax = plt.axes(projection='3d')

ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y)
plt.show()

f = lambda x, y: np.sin(x) + np.cos(x+y)

X = np.linspace(0, 5, 50)
Y = np.linspace(0, 5, 50)
X, Y = np.meshgrid(X, Y) # create a mesh grid 
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')
plt.show()