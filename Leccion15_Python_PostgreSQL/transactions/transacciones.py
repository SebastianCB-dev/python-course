import psycopg2 as pg

conn = pg.connect(user="postgres",
                  password="root",
                  host="localhost",
                  port="5432",
                  database="python_postgres")

# Con el with el commit y el rollback se ejecutan automaticamente
# Commit es cuando se ejecuta correctamente
# Rollback es cuando se ejecuta mal y se cancela la transaccion
try:
  # Que no se guarden los cambios automaticamente
  conn.autocommit = False # Si se coloca en True se omite el conn.commit(), no es buena practica

  cursor = conn.cursor()
  sentence = 'INSERT INTO people(name, last_name, email) VALUES (%s, %s, %s)'
  values = ('Maria', 'Esparza', 'mesparza@gmail.com')
  cursor.execute(sentence, values)

  sentence = 'UPDATE people SET last_name = %s WHERE id = %s'
  values = ('Gonzalez', 1)
  cursor.execute(sentence, values)

  conn.commit() # Se guardan los datos
  print('Transaction finished')
except Exception as e:
  conn.rollback()
  print('Error doing rollback:', e)
finally:
  conn.close()
  print("Connection closed")