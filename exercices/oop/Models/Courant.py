from Models.Account import Account

class Courant(Account):
    def __init__(self, number, amount, owner, credit_line):
        super().__init__(number, amount, owner)
        self.credit_line = credit_line
        
        
    def applyInterest(self):
        self.amount = self.amount + (self.amount / 0.04)