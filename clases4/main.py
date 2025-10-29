from itertools import cycle

# Herencia
class Trabajador():
    def __init__(self, nombre: str):
        self.__rut: str = ''
        self.nombre = nombre

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

class Gerente(Trabajador):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.rango = ''

juan = Trabajador('Juan')

pedro = Gerente('Pedro')
pedro.set_rut('1-1')