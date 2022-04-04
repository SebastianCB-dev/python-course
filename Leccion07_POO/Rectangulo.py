class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

base = float(input('Ingrese la base: '))
altura = float(input('Ingrese la altura: '))
rect1 = Rectangulo(base,altura)
print(f'El area del rectangulo es: {rect1.calcularArea()}')