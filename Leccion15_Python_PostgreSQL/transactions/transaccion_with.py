import psycopg2 as pg

conn = pg.connect(user="postgres",
                  password="root",
                  host="localhost",
                  port="5432",
                  database="python_postgres")

try:
  with conn:
    with conn.cursor() as cursor:
      sentence = 'SELECT name, last_name, email FROM people'
      cursor.execute(sentence)
      rows = cursor.fetchall()
      for row in rows:
        print(row)
except Exception as e:
  print('Error doing rollback:', e)
finally:
  conn.close()
  print("Connection closed")
# Output:
print('Transaction finished, commit realized')