class FiguraGeometrica(object):
    def __init__(self, alto: float, ancho: float) -> None:
        self._alto = alto
        self._ancho = ancho
    
    # Getters
    @property
    def alto(self) -> float:
        return self._alto
    
    @property
    def ancho(self) -> float:
        return self._ancho

    #setters
    @alto.setter
    def alto(self, alto: float) -> None:
        self._alto = alto

    @ancho.setter
    def ancho(self, ancho: float) -> None:
        self._ancho = ancho

    def __str__(self):
        return f'FiguraGeometrica[Alto: {self._alto}, Ancho: {self._ancho}]'
