class Account:
    def __init__(self, number, amount, owner):
        self.number = number
        self.amount = amount
        self.owner = owner
        
    def deposit(self, amount):
        if(amount > 0):
            self.amount += amount
            
    def retrait(self, amount):
        if(self.amount > amount):
            self.amount -= amount
        else:
            print("error !! solde insuffisant !")
