x = -7
if x > 0:
    print("greater than 0")
else:
    print("smaller than 0")

if x > 0 and x == 7:
    print("x is equal to 7")
    print("this will print aswell!")
elif x > 0 and x != 7:
    print("x is not equal to 7 but is greater than 0")
else:
    print("x is smaller than 0")

if x > 0 or x == -7:
    print("x is either greater than 0 or is equal to -7")

print("EOF")