

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
result = factorial(5)
print(f'El factorial de 5 es: {result}')