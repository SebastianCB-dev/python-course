import psycopg2 as pg

connection = pg.connect(user="postgres",
                        password="root",
                        host="localhost",
                        port="5432",
                        database="python_postgres")

try:
  with connection as cn:
    with cn.cursor() as cursor:
      sentence = "SELECT * FROM people WHERE person_id IN %s;"
      primary_keys = (1, 2, 3, 4, 5)
      cursor.execute(sentence, (primary_keys,))
      results = cursor.fetchall()
      for result in results:
        print(result)
except(Exception) as e:
  print("Error: unable to fetch data -", e)
finally:
  connection.close()
