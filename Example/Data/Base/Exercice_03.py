def get_int():
    value = input("enter a number ")

    while not value.isnumeric():
        value = input("enter a number ")

    return float(value)
    
nb1 = get_int()
op = input("entrer l'opérateur ")
nb2 = get_int()

if op == "+":
    print(nb1 + nb2)
elif op == "-":
    print(nb1 - nb2)
elif op == "*":
    print(nb1 * nb2)
elif op == "/":
    print(nb1 / nb2)
else:
    print("unknown operator")

print(eval("(5 ** 2) + 2"))