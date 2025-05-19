compteur = 0

while(compteur < 10):
    print("Compteur : ", compteur)
    compteur += 1
    
print("Est en dehors de mon while!")

# 0 -> 9
for i in range(10):
    print(i)
    
# 1 -> 9
for i in range(1, 10):
    print(i)
    
# 1 -> 9 (1, 3, 5, 7, 9)
for i in range(1, 10, 2):
    print(i)