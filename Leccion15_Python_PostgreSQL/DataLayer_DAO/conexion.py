import psycopg2 as pg
from logger_base import log
import sys

class Conexion:

  _DATABASE = 'python_postgres'
  _USERNAME = 'postgres'
  _PASSWORD = 'Chelsea2021!'
  _DB_PORT = '5432'
  _HOST = '127.0.0.1'
  _conexion = None
  _cursor = None

  @classmethod
  def obtenerConexion(cls):

    if cls._conexion is None:
      try:
        cls._conexion = pg.connect(host = cls._HOST,
                                   user = cls._USERNAME,
                                   password = cls._PASSWORD,
                                   port = cls._DB_PORT,
                                   database = cls._DATABASE)
        log.debug(f'Conexión con la base de datos establecida exitosamente. {cls._conexion}')
      except Exception as e:
        log.error(f'Ocurrio un error creando la conexión: {e}')
        sys.exit(1)

    return cls._conexion
  
  @classmethod
  def obtenerCursor(cls):
    if cls._cursor is None or cls._cursor.closed:
      try:
        cls._cursor = cls.obtenerConexion().cursor()
        log.debug(f'Cursor creado exitosamente. {cls._cursor}')
      except Exception as e:
        log.error(f'Ocurrio un error creando el cursor: {e}')
        sys.exit(1)
    
    return cls._cursor

if __name__ == '__main__':
  Conexion.obtenerConexion()
  Conexion.obtenerCursor()