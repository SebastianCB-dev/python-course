# Importar librerías
import psycopg2 as ps

# Crear conexión
conexion = ps.connect(user='postgres',
                      password='root',
                      host='127.0.0.1', # Localhost -> Luego cambiar a servidor donde quede la base de datos
                      port=5432,
                      dbname='test_db')
# Estado de conexion
# print('Estado conexión: ', conexion)

# Ejecutar consulta
cursor = conexion.cursor()
# Query 
sentencia = 'SELECT * FROM persona;'
cursor.execute(sentencia)
# Recuperar todos los registros
registros = cursor.fetchall()
# print(registros[0][1])
print(registros)

# Cerrar conexión y cursor
cursor.close()
conexion.close()

