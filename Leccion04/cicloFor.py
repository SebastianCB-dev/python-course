cadena = 'Hola'

#for letra in cadena:
    #print(letra)
#else:
    #print('Fin ciclo for')


# break

for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin del ciclo for')

# continue

for i in range(10):
    if i % 2 == 0:
        print(i) # 0,1,2,3,4,5...

for i in range(6):
    if i % 2 != 0 or i == 0:
        continue
    print(f'Valor: {i}')
