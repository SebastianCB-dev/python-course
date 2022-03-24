"""
 Diferencia entre tupla y lista
- La lista es modificable o mutable
- La tupla no es modificable o inmutable
"""

#Definir una tupla con parentesis NO CORCHETES
fruitList = ('Orange','Banana','Watermelon')
print(fruitList)

#Saber longitud de la tupla
print(len(fruitList))

#acceder a un elemento
print(fruitList[0])

#Navegación inversa
print(fruitList[-1])

#Acceder rango de valores sin incluir el ultimo indice
print(fruitList[0:1])

# Si solo tiene un valor agregar la coma al final
fruitListV2 = ('Apple',) 

for fruit in fruitList:
    print(fruit, end = ' ') #Imprimir con espacio

#Cambiar valor tupla
# fruitList[0] = 'Pear' ---> Error
# print(fruitList) 

# Cambiar tupla a lista
fruitTupleToList = list(fruitList)
fruitTupleToList[0] = 'Pera'
fruitList = tuple(fruitTupleToList)
print('\n' , fruitList)

#Eliminar la tupla
del fruitList
# print(fruitList)  NameError: name 'fruitList' is not defined



