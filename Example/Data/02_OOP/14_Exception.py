
class CustomException(Exception):
    pass

try:
    raise CustomException("La base de donnée n'est pas disponible")
except Exception as e:
    print(e)