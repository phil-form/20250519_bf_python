arr = ["X", "Y", "Z"] 

for i, val in enumerate(arr):
    print(i, val)

for i in [0, 1, 2, 3]:
    print(i)

for i in range(7):
    print(i)

tab = [55, 32, 75, 48, 210, 76]
for i in range(len(tab)):
    if(tab[i] == 210):
        continue
    print(tab[i])

userIn = ""

while userIn != "quit":
    # raw_input if you're using python 2.7!!
    # input will crash
    userIn = raw_input("enter quit to quit: ")
    # if you use python 3 or above input will do the work
    # and raw_input will crash!!
    # userIn = input("enter quit to quit: ")
    print(userIn)

while userIn != 5:
    userIn = int(input("enter 5 to quit: "))


for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n, " is a prime number!")