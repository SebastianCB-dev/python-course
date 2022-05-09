import os

from dominio.Pelicula import Pelicula

class CatalogoPeliculas:

  # Static
  ruta_archivo = 'peliculas.txt'

  @classmethod
  def agregar_pelicula(cls, pelicula: Pelicula) -> None:
    with open(cls.ruta_archivo, 'a', encoding='UTF-8') as archivo:
      archivo.write(f'{pelicula.nombre}\n')
    
  @classmethod
  def listar_peliculas(cls) -> None:
    with open(cls.ruta_archivo, 'r', encoding='UTF-8') as archivo:
      print('Catálogo de Películas'.center(50, '-'))
      print(archivo.read())
    
  @classmethod
  def eliminar_peliculas(cls):
    os.remove(cls.ruta_archivo)
    print(f'Archivo eliminado: { cls.ruta_archivo }')

  