from FiguraGeometrica import FiguraGeometrica as fg
from Color import Color as cl

class Cuadrado(fg, cl):
    def __init__(self, lado, color):
        # super().__init__(lado, lado)
        fg.__init__(self, lado, lado)
        cl.__init__(self, color)

    def calcular_area(self) -> float:
        return self.alto * self.ancho
