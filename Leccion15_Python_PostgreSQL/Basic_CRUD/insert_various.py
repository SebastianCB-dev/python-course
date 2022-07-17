import psycopg2 as pg

conn = pg.connect(user="postgres",
                  password="root",
                  host="localhost",
                  port="5432",
                  database="python_postgres")

try:
  with conn as cn:
    with cn.cursor() as cursor:
      sentence = "INSERT INTO people (name, last_name, email) VALUES (%s, %s, %s);"
      # Multiple records
      values = (("Miguel", "Morales", "mmorales@gmail.com"),
                ('Carlos', 'Lara', 'clara@gmail.com'),
                ('Daniel', 'Salazar', 'dsalazar@gmail.com'))
      cursor.executemany(sentence, values)
      # conn.commit() This is not necessary because it is done automatically thanks to the with statement
      inserted_records = cursor.rowcount
      print(f'Inserted records: {inserted_records}')
except(Exception) as e:
  print("Error: unable to fetch data -", e)
finally:
  conn.close()

