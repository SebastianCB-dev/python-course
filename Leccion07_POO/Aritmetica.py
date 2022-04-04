class Aritmetica:
    """
    Clase Artimetica para realizar las operacion de sumar, restar, etc.
    """
    def __init__(self, operandoA:float, operandoB: float):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA // self.operandoB

aritmetica1 = Aritmetica(1,12)
result = aritmetica1.sumar()
result2 = aritmetica1.restar()
print(f'El resultado de la suma es: {result}')
print(f'El resultado de la resta es: {result2}')
print(f'El resultado de la división es: {aritmetica1.dividir()}')
print(f'El resultado de la multiplicación es: {aritmetica1.multiplicar()}',end='')


