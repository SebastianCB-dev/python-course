# Libraries
import psycopg2 as ps

connection = ps.connect(user='postgres',
                        password='root',
                        host='127.0.0.1',
                        port=5432,
                        dbname='test_db')

# Cursor con with
try:
  with connection:
      with connection.cursor() as cursor:
        # sentencia = 'SELECT * FROM persona WHERE id_persona = %s;'
        sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
        llaves_primarias = (1, 2, 3)
        # id_persona = input('Ingrese el id de la persona: ')
        # cursor.execute(sentencia, (id_persona,))
        cursor.execute(sentencia, (llaves_primarias,))
        # registros = cursor.fetchone() #!traer todos los registros
        # ?Fetchone = traer un solo registro
        # ?Fetchall = traer todos los registros
        # ?fetchmany = traer una cantidad de registros
        registros = cursor.fetchall()
        for registro in registros:
          print(registro)
except Exception as e:
  print(f'Error: {e}')
finally:
  # Close connection
  connection.close()



