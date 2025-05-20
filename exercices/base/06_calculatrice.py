def get_int(text):
    ret_val = 0
    return_set = False
    while not return_set:
        try:
            ret_val = int(input(text))
            return_set = True
        except ValueError:
            print("Vous devez rentrer un nombre!")
    return ret_val

# a et b vont être des entiers
stop = 0

while stop == 0:
    a = get_int("Entrer le premier nombre : ")

    operator = ""

    # l'opérateur sera une string égale à "+" "-" "/" "*"
    # initialisation de l'opérateur
    # while operator not in ["+", "-", "*", "/"]:
    while operator != "+" and operator != "-" and operator != "*" and operator != "/":
        operator = input("Entrer l'opérateur : ")

    b = get_int("Entrer le second nombre : ")

    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Error division par zéro")

    stop = get_int("Voulez vous continuer ? 0/1")
