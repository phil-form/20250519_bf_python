
try:
    nbr = int(input("Entrez un nombre : "))
except ValueError:
    print("vous devez rentrer un nombre !")
    
def get_int(text):
    ret = 0
    return_set = False
    
    while not return_set:
        try:
            ret = int(input(text))
            return_set = True
        except ValueError:
            print("Vous devez rentrer un nombre!")
            
    return ret