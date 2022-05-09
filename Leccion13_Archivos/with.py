# Archivos con with

# __enter__ -> Abre el recurso
# __exit__ -> Cierra el recurso 
# with open('prueba.txt', 'r', encoding='UTF-8') as archivo:
from manejo_archivos import ManejoArchivos


with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
    # Luego se llama el metodo __exit__





