from Cuadrado import Cuadrado
# from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo
# No se puede instanciar una clase abstacta
# figura = FiguraGeometrica()

print('Creacion objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5, 'Rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(9, 8, 'Azul')
rectangulo1.ancho = 15
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# Method resulution order
print(Cuadrado.mro())
