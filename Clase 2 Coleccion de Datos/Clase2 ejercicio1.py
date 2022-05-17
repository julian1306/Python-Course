lista1 = [1, 12, 123]
lista2 = ["Bye","Ciao","Agur","Adieu"]

# variable.append agrega el ultimo
lista1.append (int(1234))
lista1.append ("Hola")

lista2.append ("Adios")
lista2.append (int(1234))

print(lista1)
print(lista2)

#slicing -1 es el ultimo
lista3 = lista1[:-1]


print(lista3)
#slicing seleciona el 1 y arranca -1 ultimo
lista4 = lista2 [1:-1]

lista5 = lista4 + lista3

print(lista5)

print(lista4)


