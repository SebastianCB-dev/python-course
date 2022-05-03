"""
w = write
r = ride
a = add
x = create

t = Text
b = Binary

w+ = Escribir y leer
r+ = Leer y escribir 
"""

try:
    archivo = open('prueba.txt', 'w',encoding='UTF-8')
    archivo.write('Chelsea F.C. the best team in the world\n')
    archivo.write('Final line')
except Exception as e:
    print(f'No se pudo abrir el archivo por: {e}')
finally:
    archivo.close()
    print('Fin del archivo')

