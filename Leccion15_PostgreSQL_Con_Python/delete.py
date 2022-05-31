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
      sentencia = 'DELETE FROM persona WHERE id_persona=%s;'
      valores = (7,)
      cursor.execute(sentencia, valores)
      registros_borrados = cursor.rowcount
      # No hace falta hacer commit porque no se hace ninguna transaccion
      print(f'Registros Borrados: {registros_borrados}')

except Exception as e:
  print(f'Error: {e}')
finally:
  # Close connection
  connection.close()  
