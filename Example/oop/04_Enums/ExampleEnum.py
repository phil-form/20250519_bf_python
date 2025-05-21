from enum import Enum

class Colors(Enum):
    RED = '1'
    BLEU = '2'
    GREEN = '3'
    YELLOW = '4'
    
# stocker '2' dans col 
col = Colors.BLEU.value
# stocker 'BLUE' dans enumName
enumName = Colors.BLEU.name