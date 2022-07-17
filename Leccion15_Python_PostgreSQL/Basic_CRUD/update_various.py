import psycopg2 as pg

conn = pg.connect(user="postgres",
                  password="root",
                  host="localhost",
                  port="5432",
                  database="python_postgres")

try:
  with conn as cn:
    with cn.cursor() as cursor:
      sentence = "UPDATE people SET email = %s WHERE person_id = %s;"
      values = (("myemail@gmail.com", 7), ("myemail2@gmail.com", 8))
      cursor.executemany(sentence, values)
      # Commit is not necessary because it is done automatically thanks to the with statement
      updated_records = cursor.rowcount
      print(f'Updated records: {updated_records}')
except(Exception) as e:
  print("Error: unable to fetch data -", e)
finally:
  conn.close()