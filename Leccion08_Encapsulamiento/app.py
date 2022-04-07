from Persona import Persona
#from Persona import * -> Importar todo clases, funciones, variables

print('Creación objetos'.center(50,'-')) # Imprimir centrado con 50 de caracteres -
persona1 = Persona('Joan', 'Carrillo', 20)
persona1.nombre = 'Joan Sebastian'
persona1.edad = 21
persona1.apellido = 'Carrillo Barón'
print(persona1.nombre, persona1.apellido, persona1.edad)

print('Eliminación objetos'.center(50, '-'))
del persona1