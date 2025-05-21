tab = [5, 9, 4, 3, 7, 2, 3, 1]

for elem in tab:
    print(elem)

print(tab)

dict_1 = {"paire": [], "impaire": []}

for elem in tab:
    if(elem % 2) == 0:
        dict_1["paire"].append(elem)
    else:
        dict_1["impaire"].append(elem)

print(dict_1)