# Diccionario
# Esta compuesto por (key, value)

diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    "DBMS": 'Database Management System'
}
print(diccionario)

#Longitud diccionario
print(len(diccionario))

# Obtener información
print(diccionario.get('IDE'))
print(diccionario['OOP'])

# modificar elementos
diccionario['IDE'] = "INTEGRATED DEVELOPMENT ENVIRONMENT"
print(diccionario)

print("___________________________")
# Recorrer elementos
for key,value in diccionario.items():
    print(key, value)

for key in diccionario.keys():
    print(key)

for value in diccionario.values():
    print(value)

# Comprobar existencia de algún elemento
print('IDE' in diccionario)

# Agregar elemento
diccionario['PK'] = 'Primary Key'
diccionario['FK'] = 'Foreign Key'

# Remover elemento
diccionario.pop('FK')

#Limpiar diccionario
diccionario.clear()
print(diccionario)

# Eliminar variable 
del diccionario
# print(diccionario) ---> !Error name "diccionario" is not defined