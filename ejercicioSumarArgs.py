"""
Crean una funcion para sumar los valores recibidos de tipo numerico
utilizandno argumento variables *args como parametro de la funcion
y regtresar como resulado la sima de todos los valores pasados como argumentos
"""


# Definir funcion para sumar valores
def sumarValores(*args):
    resultado = 0
    # iterar cada elemento de los elementos variables
    for valor in args:
        # resultado = resultado + valor
        resultado += valor
    return resultado


# LLamar a la funcion


print(sumarValores(3, 6, 8, 9, 7, -4))
