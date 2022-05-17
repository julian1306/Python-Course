def año_bisiesto(numero):

    while True:

        if numero.isnumeric():
            numero = int(numero) #---------------------------------------------- LA CLAVE fuerza el valor a int
            if numero % 4 == 0 and (numero % 100 != 0 or numero % 400 ==0):
                numero = input("es bisiesto ingrese otro : ")
            else:
                numero = input("NO es bisiesto ingrese otro : ")

        elif numero == "exit": #-----------por si queres salir del programa porque ? no hay porque
            break
        else:
            numero = input("ingrese dato valido : ")
    else:
        pass


############################################################

año = input("ingrese año : ")

año_bisiesto(año)
