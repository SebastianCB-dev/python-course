import psycopg2 as pg

conn = pg.connect(user="postgres",
                  password="root",
                  host="localhost",
                  port="5432",
                  database="python_postgres")

try:
  with conn as cn:
    with cn.cursor() as cursor:
      sentence = "DELETE FROM people WHERE person_id IN %s;"
      # sentence = "DELETE FROM people WHERE person_id = %s;"
      values = (13,)
      various_values = (13,14, 15)
      cursor.execute(sentence, (various_values, ))
      # Commit is not necessary because it is done automatically thanks to the with statement
      deleted_records = cursor.rowcount
      print(f'Deleted records: {deleted_records}')
except(Exception) as e:
  print("Error: unable to fetch data -", e)
finally:
  conn.close()