from FiguraGeometrica import FiguraGeometrica 
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        Color.__init__(self, color)
        FiguraGeometrica.__init__(self, lado, lado)

    def calcular_area(self) -> float:
        return (self.alto * 2 ) + (self.ancho * 2)

    def __str__(self):
        return f'{super().__str__()} Cuadrado[Lado: {self.ancho}]'
