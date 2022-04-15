from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5,'Blue')
print(cuadrado1.color)
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.calcular_area())

# MRO - Method Resolution Order
# Jerarquía de clases, herencia, orden de busqueda
print(Cuadrado.mro())