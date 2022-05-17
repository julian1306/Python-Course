



def año_bisiesto(numero):

    if not numero % 4 and (numero % 100 or not numero % 400):
        return print('año bisiesto')
    else:
        return print('año no bisiesto')




################################################

año = input('Ingrese un año:')

while not año.isnumeric():
    año = input("Ingrese año Valido : ")

año = int(año)      #----------------- LA CLAVE convierte el año en int
año_bisiesto(año)



