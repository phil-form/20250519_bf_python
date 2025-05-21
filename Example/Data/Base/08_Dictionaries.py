dico = { "entry_1": 153, "entry_2": "test", "entry_3": 12.5 }
print(dico["entry_1"])
print(dico["entry_2"])
print(dico["entry_3"])
dico["entry_4"] = 253
print(dico["entry_4"])

for i in dico.items():
    print(i)

for key, val in dico.items():
    print("key : ", key, " val : ", val)

names = ["Bach", "Bruckner", "Vieuxtemps", "Wagner"]
birthdate = [1685, 1824, 1820, 1813]

dict_2 = { k:v for k, v in enumerate(names) }
print(dict_2)

dict_3 = { name:bd for name, bd in zip(names, birthdate) if bd < 1824 }
print(dict_3)