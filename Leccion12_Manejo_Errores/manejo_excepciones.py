from NumerosIdenticosException import NumerosIdenticosException
resultado = None
a = 10
b = 0

try:
    x = int(input("Primer numero: "))
    y = int(input("Segundo numero: "))
    if x == y:
        raise NumerosIdenticosException('Números identicos')
    resultado = x / y
except ZeroDivisionError as zde:
    # print(list(e.args)[0])
    print("Error tipo ZeroDivisionError: ", zde, type(zde))
except TypeError as te:
    print("Error tipo TypeError: ", te)
#except ValueError as ve:
#    print("Error tipo ValueError")
except Exception as e:
    print("Error tipo Exception", e)
else:
    # Si no se llama ninguna exception
    print('No se arrojó ninguna excepción')
finally:
    # Independientemente si se arroja error o no se ejecuta
    print('Ejecución del bloque Finally')
print(resultado)
print('Continuamos')


