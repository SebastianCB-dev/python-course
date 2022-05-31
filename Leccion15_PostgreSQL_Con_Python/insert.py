# libraries
import psycopg2 as ps

connection = ps.connect(user='postgres',
                        password='root',
                        host='127.0.0.1',
                        port=5432,
                        dbname='test_db')
try:
  with connection:
    with connection.cursor() as cursor:
      sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s);'
      valores = ('Holman', 'Barón', 'hdbolivar@gmail.com')
      cursor.execute(sentencia, valores)
      # connection.commit() # Guarda los cambios en la base de datos
      # ! Con with el commit se hace automáticamente
      registros_insertados = cursor.rowcount
      print(f'Registros insertados: {registros_insertados}')
  

except Exception as e:
  print(f'Error: {e}')
finally:
  # Close connection
  connection.close()
  
