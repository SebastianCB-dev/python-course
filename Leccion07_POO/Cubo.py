class Cubo:
    def __init__(self, alto: float, ancho: float, profundidad: float):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.alto * self.ancho * self.profundidad

alto = float(input('Ingrese el alto: '))
ancho = float(input('Ingrese el ancho: '))
profundidad = float(input('Ingrese la profundidad: '))

cubo1 = Cubo(alto,ancho,profundidad)
print(f'El volumen es {cubo1.calcular_volumen()}')