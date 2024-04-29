class Aritmetica:
    """
    Clase Aritmetica para realizar operaciones de sumar, restar, etc.
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multipolicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return (self.operandoA /
                self.operandoB)
aritmetica1 = Aritmetica(10,3)
print(f'Sumar: {aritmetica1.sumar()}')
print(f'Restar: {aritmetica1.restar()}')
print(f'Multiplicar: {aritmetica1.multipolicar()}')
print(f'Dividir: {aritmetica1.dividir():.2f}')
