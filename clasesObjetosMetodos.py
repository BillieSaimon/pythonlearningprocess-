class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Pessona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrar_detalle()

persona2 = Persona('Karla', 'Garcia', 32)
persona2.mostrar_detalle()
