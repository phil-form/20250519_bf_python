nbr1 = 0
nbr2 = 1

for i in range(10):
    print(nbr1)
    nbr1, nbr2 = nbr2, nbr1 + nbr2
    # tmp = nbr1
    # nbr1 = nbr2
    # nbr2 = tmp + nbr2
