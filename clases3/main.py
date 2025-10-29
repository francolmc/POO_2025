# Propiedades
class Departamento():
    def __init__(self):
        self.__codigo_departamento: str = ''
        self.nombre = ''

    # Propiedad getter
    @property
    def codigo_departamento(self) -> str:
        return self.__codigo_departamento
    
    # Propiedad setter
    @codigo_departamento.setter
    def codigo_departamento(self, value: str) -> None:
        self.__codigo_departamento = value

finanzas = Departamento()
finanzas.codigo_departamento = '0001-2'
