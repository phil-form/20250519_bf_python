from Models.Account import Account
from datetime import datetime

class Epargne(Account):
    def __init__(self, number, amount, owner):
        super().__init__(number, amount, owner)
        self.last_date = datetime()
        
    def retrait(self, amount):
        super().retrait(amount)
        self.last_date = datetime()
        
    def applyInterest(self):
        self.amount += self.amount * 0.09
