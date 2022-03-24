# Un set no mantiene un orden
# Y no permite almancenar datos duplicados
# No permite modificar elementos
# Si deja eliminar
# Si deja agregar

#! Set
#Definir set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)

#Longitud set
print(len(planetas))

#Revisar si un elemento está presente
print('Marte' in planetas) # True or False

# Agregar un elemento
planetas.add('Tierra')
print(planetas)

# No soporta elementos duplicados
planetas.add('Tierra')

# Eliminar elemento
planetas.remove('Tierra') # Si no existe, lanzará error KeyError
print(planetas)
planetas.discard('Júpiter') # elimina y no arroja error en caso de no existir la key
print(planetas)

# Eliminar todos los datos o limpiar el set
planetas.clear()
print(planetas)

# Eliminar variable planetas
del planetas
