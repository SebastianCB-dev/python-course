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
      values = ("Carlos", "Sanchez", "csanchez@gmail.com")
      # name = input("Enter name: ")
      # lastname = input("Enter lastname: ")
      # email = input("Enter email: ")
      cursor.execute(sentence, values)
      conn.commit() # Commit the changes to the database
      inserted_records = cursor.rowcount
      print(f'Inserted records: {inserted_records}')
except(Exception) as e:
  print("Error: unable to fetch data -", e)
finally:
  conn.close()