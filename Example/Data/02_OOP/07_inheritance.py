class BaseClass:
    def __init__(self, msg) -> None:
        self.__msg = msg
    
    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, msg):
        self.__msg = msg

    def method_override(self):
        print("this is print from the base class")

class DerivedClass(BaseClass):
    def __init__(self, msg, value) -> None:
        super().__init__(msg)
        self.__val = value

    @property
    def value(self):
        return self.__val

    @value.setter
    def value(self, value):
        self.__val = value

    def method_override(self):
        print("this method is overridden")

class OtherClass:
    pass

print("Is DerivedClass related to BaseClass ? ", issubclass(DerivedClass, BaseClass))
print("Is DerivedClass related to OtherClass ? ", issubclass(DerivedClass, OtherClass))

obj = DerivedClass("my secret message", 2)
for i in range(obj.value):
    print(obj.msg)

obj.msg = "my super secret message"
obj.value = 3
for i in range(obj.value):
    print(obj.msg)
obj2 = BaseClass("this is great!!")
obj2.method_override()
obj.method_override()