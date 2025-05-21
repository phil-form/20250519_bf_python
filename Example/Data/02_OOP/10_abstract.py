from abc import ABC, abstractmethod
from datetime import datetime

class AbstractClass(ABC):

    @abstractmethod
    def abstractMethod(self, msg):
        pass

    def ma_fonction():
        print("test")
    
class Derived(AbstractClass):
    def abstractMethod(self, msg):
        print(msg)

    
test = Derived()
test.abstractMethod("message")
