array = []
#! Si se consume toda la información con el readlines el archivo quedara vacio
try:
    # archivo = open('c:\\sebastiancb...')
    archivo = open('prueba.txt', 'r', encoding='UTF-8')
    array = archivo.readlines() # Array
    cinco_caracteres = archivo.read(5)
    print(cinco_caracteres)
    tres_caracteres = archivo.read(3) # Leer 3 caracteres
    print(tres_caracteres)
    print(array) 
except Exception as e:
    print(f'Error abriendo el archivo, {e}')
finally:
    archivo.close()



#Quitar \n en la lectura
array = [line.replace("\n", "") for line in array]
print(array)


