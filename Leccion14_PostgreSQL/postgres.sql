-- Common commands:
-- \l                            list all databases
-- \c [nombre_base_de_datos]     create database

-- Queries
CREATE TABLE people(
  person_id SERIAL NOT NULL PRIMARY KEY, -- SERIAL = autoincrement
  name      CHARACTER varying(10485760) NOT NULL,
  last_name CHARACTER varying(10485760) NOT NULL,
  email     CHARACTER varying(10485760) NOT NULL
);

-- Insertar datos
INSERT INTO people(name, last_name, email) VALUES
('Joan Sebastián', 'Carrillo Barón', 'jscarrillo02@ucatolica.edu.co'),
('Juan David', 'Mejia Morales', 'jdmejia94@gmail.com'),
('Diego Alejandro', 'Clavijo Ladino', 'daclavijo93@gmail.com'),
('Deiver Camilo', 'Mena Mosquera', 'xcamilx@gmail.com'),
('Oscar Mauricio', 'Correa', 'mauroc80@gmail.com'),
('Juan Pablo', 'Perez', 'jperez@gmail.com');

-- Algunos datos con valores nulos
INSERT INTO people(name, last_name, email) VALUES
('Juan Pablo', 'Perez', NULL),
('Santiago', NULL, 'santi@gmail.com'),
(NULL, 'Musk', 'emusk@gmail.com');

SELECT * FROM public.people ORDER BY person_id ASC; -- Show all people

-- Basic queries
SELECT * FROM public.people WHERE person_id = 1; -- Show person with id 1
SELECT * FROM public.people WHERE person_id IN(1, 2, 3); -- Show people with id 1, 2 and 3
SELECT * FROM public.people WHERE person_id NOT IN(1, 2, 3); -- Show people without id 1, 2 and 3

-- Update
UPDATE public.people SET 
name = 'Juan Carlos', last_name = 'Barrero Calixto', email = 'jcbarrero@ucatolica.edu.co' 
WHERE person_id = 7; -- Update person with id 1

-- Delete
DELETE FROM public.people WHERE person_id = 8; -- Delete person with id 8 
DELETE FROM public.people WHERE person_id IN (); -- Delete all people
DELETE FROM public.people WHERE person_id IN (1, 2, 3); -- Delete people with id 1, 2 and 3