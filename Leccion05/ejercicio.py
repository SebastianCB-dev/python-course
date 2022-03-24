#Iterar un rango de 0 a 10  e imprimir sólo los números divisibles entre 3
array = []
for i in range(0,11):
    if i % 3 == 0 and i != 0:
        array.append(i)


print(array)