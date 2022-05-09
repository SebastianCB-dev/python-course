class Pelicula(object):
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    def __str__(self) -> str:
        return f'Pelicula : { self._nombre }'
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    