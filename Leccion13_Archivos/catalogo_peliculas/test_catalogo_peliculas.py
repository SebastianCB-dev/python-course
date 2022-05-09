
from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
  print('Opciones: ')
  print('1. Agregar Película')
  print('2. Listar Películas')
  print('3. Eliminar Catálogo De Películas')
  print('4. Salir')
  try:
    opcion = int(input('Escribe tu opción (1-4): '))
  except Exception as e:
    print('La opción debe ser un numero!!!')
  
  if opcion == 1:
    nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
    pelicula = Pelicula(nombre_pelicula)
    cp.agregar_pelicula(pelicula)
  elif opcion == 2:
    cp.listar_peliculas()
  elif opcion == 3:
    cp.eliminar_peliculas()
  else:
    if opcion != 4:
      print('Opción no válida!')
else:
  print('Salimos del programa')