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
      sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s;'
      valores_nuevos = ('Juan Jose', 'Cuervo', 'jcuervo@gmail.com', 2)
      cursor.execute(sentencia, valores_nuevos)
      registros_actualizados = cursor.rowcount
      print(f'Registros Actualizados: {registros_actualizados}')      

except Exception as e:
  print(f'Error: {e}')
finally:
  # Close connection
  connection.close()  


# ! Para actualizar varios registros
sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s;'
valores_nuevos(('a', 'b', 'c', 1),
               ('a', 'b', 'c', 2),
               ('a', 'b', 'c', 3),
               ('a', 'b', 'c', 4))
cursor.executemany(sentencia, valores_nuevos)
registros_actualizados = cursor.rowcount
print(f'Registros Actualizados: {registros_actualizados}')
      