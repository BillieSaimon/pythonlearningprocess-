def sumar(a = 0, b = 0) -> int:
    return a + b

resultado = sumar()
print(f'Resultado de la suma: {sumar()}')

print(f'Resultado de la suma: {sumar(2, 8)}')

def listaNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listaNombres('Juan', 'Karla', 'Maria', 'Ernesto', 'Simon')
listaNombres('Laura', 'Carlos')