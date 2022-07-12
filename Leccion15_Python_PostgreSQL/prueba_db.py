import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="root",
                              host="localhost", # O bien host="127.0.0.1",
                              port="5432",
                              database="test_db");

# If the connection is successful, it will print the connection object
# else it will print the error message
# print( connection )

try:
  with connection as conn:
    with conn.cursor() as cursor:
      sentence = "SELECT * FROM people;"
      cursor.execute(sentence)
      registros = cursor.fetchall()
      print(registros)
except(Exception) as e:
  print("Error: unable to fetch data -", e)
finally:
  connection.close()

