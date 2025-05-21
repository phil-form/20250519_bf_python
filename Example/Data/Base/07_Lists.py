list = ["entry1", 123, 12.5]
# instert at the end
list.append(55)
# insert the new item at the chose index
list.insert(2, "I want a new item")

for i in range(len(list)):
    print(list[i])
    
print("\n")

list2 = ["list 2", 7225, "end of list 2"]
list3 = list + list2
for i in range(len(list3)):
    print(list3[i])

list_2 = [i ** 2 for i in range(10)]

print(list_2)