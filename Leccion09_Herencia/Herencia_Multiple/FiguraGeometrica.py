class FiguraGeometrica(object):
    def __init__(self, ancho: float, alto: float)-> None:
        self._ancho = ancho
        self._alto = alto

    # Getters
    @property
    def ancho(self) -> float:
        return self._ancho
    
    @property
    def alto(self) -> float:
        return self._alto
    
    # Setters
    @ancho.setter
    def ancho(self, ancho: float) -> None:
        self._ancho = ancho
    
    @alto.setter
    def alto(self, alto: float) -> None:
        self._alto = alto