class Voiture:
    def __init__(self) -> None:
        self.__roues = 4

    def _get_roues(self):
        return self.__roues

    def _set_roues(self, value):
        if isinstance(value, int):
            self.__roues = value

    roues = property(_get_roues, _set_roues)

voit = Voiture()
print(voit.roues)
voit.roues = 6
print(voit.roues)

class Camion:
    def __init__(self) -> None:
        self.__roues = 6

    @property
    def roues(self):
        return self.__roues

    @roues.setter
    def roues(self, value):
        self.__roues = value

cam = Camion()
print(cam.roues)
cam.roues = 8
print(cam.roues)


