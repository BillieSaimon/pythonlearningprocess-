"""
El siguiente ejercicio es para calcular el área de un cuadrado y el perímetro de este
Para esto se le pedirá a el usuario que proporcione el alto de la figura y también el ancho
Posteriormente a eso el programa imprimirá el resultado en el siguiente formato no usar  acentos
y respetar los espacios, mayúsculas, minúsculas y saltos de linea

"""
alto = int(input("Proporcione el alto de la figura: "))
ancho = int(input("Proporcione el ancho de la figura: "))
perimetro = 2*(alto + ancho)
area = alto * ancho
print(f'El area es: {area}')
print(f'El perimetro es: {perimetro}')
