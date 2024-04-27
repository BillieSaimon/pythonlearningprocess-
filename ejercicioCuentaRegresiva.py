"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1
En caso de pasar el valor de 3, debe imprimir:
3
2
1
Si se pasan valores negativos no imprime nada

"""


def descender(numero):
    if numero >= 1:
        print(numero)
        descender(numero - 1)
    elif numero < 0:
        print('Valor incorrecto')
    else:
        return 1


descender(int(input('Dame un numero positivo menor a 999: ')))
