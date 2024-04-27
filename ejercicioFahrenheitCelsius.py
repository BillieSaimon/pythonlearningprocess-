"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celcius a fahrenheit y veceversa
"""
conversion = None


# Definir funcion que convierte de Fahrenhet a Celsius


def celsius(grados_f):
    conversion = (grados_f - 32) * 5 / 9
    print(f'{grados_f} grados Fahrenheit son {conversion:.2f} grados Celsius')


# Definir funcion que convierte de Celsuis a Fahrenheit


def fahrenheit(grados_c):
    conversion = (grados_c * 1.8) + 32

    print(f'{grados_c} grados Celsius son {conversion:.2f} grados Fahrenheit')


opcion = input('Quieres obtener celcius o fahrenheit? (F o C): ')
if opcion == 'C':
    grados_f = int(input('Ingeresa los grados fahrenheit que quieres pasar a celsius: '))
    celsius(grados_f)

elif opcion == 'F':
    grados_c = int(input('Ingeresa los grados celsius que quieres pasar a fahrenheit : '))
    fahrenheit(grados_c)
