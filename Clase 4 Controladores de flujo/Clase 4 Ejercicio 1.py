
edad = input('ingrese su edad ')

if edad.isnumeric():
    edad = int(edad)
    if edad >= 18:
        print('usted es mayor de edad')
    else:
        print('usted es menor de edad')

else:
    print('ingrese edad valida')
