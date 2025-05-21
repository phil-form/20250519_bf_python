d1 = {'a' : 15,'b' : 18,'c' : 20}

for i,j in enumerate(d1):
    print(i,j)
    print(i,j, d1[j])

for i,(k, v) in enumerate(d1.items()):
    print(i,k, v)