class Person:
    def __init__(self, data):
        self.lastname = data['lastname']
        self.firstname = data['firstname']
        
    def __repr__(self):
        return '{"lastname": "' + self.lastname + '", "firstname": "' + self.firstname + '" }'