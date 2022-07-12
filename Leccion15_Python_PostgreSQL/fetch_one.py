import psycopg2 as pg

connection = pg.connect(user="postgres",
                        password="root",
                        host="127.0.0.1",
                        port="5432",
                        database="python_postgres")
try:
  with connection as cn:
    with connection.cursor() as cursor:
      sentence = "SELECT person_id, name FROM people WHERE person_id = %s;"
      person_id = input('Enter a person_id: ')
      cursor.execute( sentence, (person_id,) ) # Cause' the tuple has only one element, we have to add a comma
      results = cursor.fetchone()
      print(results)
except(Exception) as e:
  print("Error: unable to fetch data -", e)
finally:
  connection.close()

