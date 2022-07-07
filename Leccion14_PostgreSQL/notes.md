# PostgreSQL

1. Convertirse en usuario postgres 
sudo su - postgres

2. Crear ambiente
initdb --locale en_US.UTF-8 -D /var/lib/postgres/data

3. Conectarse
psql --username=freecodecamp dbname=postgres
psql -U postgres 

4. Listar bases de datos
\l

5. crear base de datos
CREATE DATABASE database_name;

6. Conectar a base de datos
\c database_name

7. Ver tablas de una base de datos
\d

8. Ver descripcion de una tabla especifica en una base de datos
\d table_name;

9. Crear tabla
CREATE TABLE table_name();

10. Add column into a table
ALTER TABLE table_name ADD COLUMN column_name DATATYPE;

11. Remove column from a table
ALTER TABLE table_name DROP COLUMN column_name;

12. Renombrar campo de una table
ALTER TABLE table_name RENAME COLUMN column_name TO new_name;

13. Insertar datos en una tabla
INSERT INTO table_name(column_1, column_2) VALUES (value1, value2)

14. Mostrar todos los datos de una tabla
SELECT * FROM table_name

15. Eliminar un dato de una tabla
DELETE FROM table_name where <condition>;

16. Eliminar una tabla
DROP TABLE table_name;

17. Renombrar base de datos
ALTER DATABASE database_name RENAME TO new_database_name;

18. Actualizar un dato
UPDATE table_name SET column_name=new_value WHERE condition;

19. PRIMARY KEY.
It's a column that uniquely identifies each row in the table
ALTER TABLE table_name ADD PRIMARY KEY (column_name);

20. Eliminar PRIMARY KEY.
ALTER TABLE table_name DROP CONSTRAINT constraint_name;

## Comentarios
Usando: --