class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
# Pour déclencher une exception vous devez utiliser raise suivit du nom de l'exception et de ses arguments    
raise MyException("Hello")