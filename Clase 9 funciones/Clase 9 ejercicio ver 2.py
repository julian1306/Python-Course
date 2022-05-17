
def anio_bisiesto(numero):

    if numero.isnumeric():
        numero = int(numero)
        if numero % 4 == 0 and (numero % 100 != 0 or numero % 400 == 0):
            return print("es bisiesto")
        else:
            return print("NO es bisiesto")
    else:
        return print("ingrese numero valido ")



anio = input("ingrese anio : ")

anio_bisiesto(anio)

