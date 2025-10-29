# Estrucutura basica de una clase
class Persona:
    # Constructor
    def __init__(self):
        self.nombre: str = ""
        self.nivel: int = 0

    # Metodo
    def presentate(self) -> None:
        print(f"Hola, soy {self.nombre}")


# Instanciar
pedro = Persona()
pedro.nombre = "Pedro Rojas"
pedro.nivel = 50
pedro.presentate()

franco = Persona()
franco.nombre = "Franco Morales"
franco.nivel = 55
franco.presentate()
