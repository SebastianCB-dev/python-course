
class Persona(object):
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, sueldo: float) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}, Sueldo: {self.sueldo}'