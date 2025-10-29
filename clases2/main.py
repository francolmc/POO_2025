from itertools import cycle

# Encapsulamiento
class Trabajador():
    def __init__(self):
        self.__rut: str = ''

    def get_rut(self) -> str:
        return self.__rut
    
    def set_rut(self, value: str) -> None:
        reversed_digits = map(int, reversed(str(value.split('-')[0])))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        dv = (-s) % 11
        if str(dv) != value.split('-')[1]:
            raise ValueError('El RUT no es valido')
        self.__rut = value


carlos = Trabajador()
carlos.set_rut('21567244-1')