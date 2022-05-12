# Importar librerías
import psycopg2 as ps

conexion = ps.connect(user='postgres',
                      password='admin',
                      host='127.0.0.1',
                      port=5432,
                      dbname='test_db')
print('Estado conexión: ', conexion)
cursor = conexion.cursor()

sentencia = 'SELECT * FROM persona;'

cursor.execute(sentencia)
registros = cursor.fetchall()

print(registros)

cursor.close()
conexion.close()

