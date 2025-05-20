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

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def is_even(nbr):
    if(nbr % 2 == 0):
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")
        
def is_even_v2(nbr):
    if(nbr % 2 == 0):
        return True
    else:
        return False
        
def is_even_v3(nbr):
    return nbr % 2 == 0
        
temp = 25
f_temp = celsius_to_fahrenheit(temp)
print(f_temp)

my_other_func("Il fait beau aujourd'hui ")
print(function_name(9, 42))

nbr = get_int("Entrez un entier : ")