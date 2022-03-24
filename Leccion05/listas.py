#Definir una lista de tipo string
nombres = ['Sebastian', 'Jairo', 'Daniel', 'Juan']
#imprimir la lista nombres
print(nombres)
#Acceder a elementos de una lista
print(nombres[0])
print(nombres[1])
# Acceder a los elementos de manera inversa
print(nombres[-1]) #Ultimo valor de la lista
print(nombres[-2]) #Penultimo

#Imprimir rango
print(nombres[0:2]) # Recupera el indice 0 y 1 sin incluir el indice 2

# Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
print (nombres[-1:])

#Desde el indice indicado hasta el final
print(nombres[1:])

#Cambiar Valor especificando un indice
nombres[3] = 'Juan David'
print(nombres)

#Iterar una lista
for idx, nombre in enumerate(nombres):
    print(nombre, idx)
else:
    print('No existen mas nombres en la lista')

#Preguntar el largo de una lista
print("El arreglo nombres tiene: " + str(len(nombres)) + " elementos.")

#Agregar un elemento
nombres.append("Eduardo")
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(1, 'Diego')
print(nombres)

# Remover un elemento
nombres.remove('Eduardo')
print(nombres)

# Remover ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice
del nombres[0]
print(nombres)

# Limpiar lista
nombres.clear()
print(nombres)

# Borrar lista por completo
del nombres
# print(nombres) -> Error