# dict (Key, Value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
# largo
print(len(diccionario))
# accedere a elemento
print(diccionario['IDE'])
# otra forma de recuperar elemento
print(diccionario.get('OOP'))
# modificar elementos
# diccionario['IDE'] = 'integrated development environment'
print(diccionario)
# recorrer elementos termino y valor
for termino, valor in diccionario.items():
    print(termino, valor)
# recorrer elementos solo las llaves
for termino in diccionario.keys():
    print(termino)
# recorrer elementos valor asociado a los terminos
for valor in diccionario.values():
    print(valor)
# comprobar exsitencia de algun elemento
print('IDE' in diccionario)
# agregar elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
# remover elemento
diccionario.pop('DBMS')
print(diccionario)
# limpiar
diccionario.clear()
print(diccionario)
# elimianar el diccionario
del diccionario
# print(diccionario)
