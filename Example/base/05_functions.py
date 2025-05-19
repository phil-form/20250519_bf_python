from random import randint

def function_name(param1, param2):
    return param1 ** param2

function_name(12, 23)

def my_other_func(text):
    lastname = input("Enter your lastname : ") 
    print(text + lastname)
    
def get_int(text):
    return int(input(text))

def sq(nbr):
    # return nbr * nbr
    return nbr ** 2

my_other_func("Il fait beau aujourd'hui ")
print(function_name(9, 42))

nbr = get_int("Entrez un entier : ")