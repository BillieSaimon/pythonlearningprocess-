"""
Ejercicio: Calculadora de impuestos
crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado
#Formula: pago_total = pago_sin_impuesto + pago sin impuesto * (impuesto/100)
"""


# Definimos la funcion


def pagoImpuestos(pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto / 100)
    print(f'Usted debe pagar {pagoTotal} de impuestos')


# Se ejecuta la funcion
# pagoImpuestos(float(input('Proporcione el pago sinimpuesto:')), float(input('Proporcione el monto del impuesto: ')))

pagoSinImpuesto = float(input('Proporcione el pago sinimpuesto:'))
impuesto = float(input('Proporcione el monto del impuesto: '))
pagoImpuestos(pagoSinImpuesto, impuesto)
