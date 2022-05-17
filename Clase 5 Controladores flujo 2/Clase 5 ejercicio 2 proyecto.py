# 1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
#
#
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# En caso de no introducir una opción válida, el programa informará de que no es correcta.



numero_1 = int(input("ingrese numero N1 : "))
numero_2 = int(input("ingrese numero N2 : "))

x = 1

while x == 1 :

    opcion = int(input("""ingrese opcion deseada :
     1 -  Suma los dos numeros
     2 - resta los dos numeros 
     3 - multiplica los dos numeros 
     4 - Salir del programa 
     """))
    if opcion == 1:
        suma = numero_1 + numero_2
        print(suma)

    elif opcion == 2:
        resta = numero_1 - numero_2
        print(resta)

    elif opcion == 3:
        multiplicacion = numero_1 * numero_2
        print(multiplicacion)

    elif opcion == 4:
        break
    elif opcion < 1 or opcion > 4:
        print("opcion no valida")

else:
    pass


# Escribí un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

x = 1

while x == 1:
    numero = int(input("ingrrse numero impar : "))

    if numero % 2 != 0:
        print("correcto es un numero impar")
        break
    else:
        print( " !!! incorrecto intente de nuevo !!! ")
else:
    pass


#3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

suma = sum(range (1, 100, 2 ))
print(suma)


#4 ejercicio 4



lista = []


cuantos_numeros = int(input("cuantos numeros desea ingresar ? :"))
contador = 0


while cuantos_numeros != contador:
    contador += 1
    print('Introduzca num:', contador)
    numero = int(input())
    lista.append(numero)

else:
    promedio = sum(lista) / int(cuantos_numeros)
    print("promedio :", promedio)


#5) Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso.
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
#🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

lista = [1, 3, 6, 9]

numero = int(input("ingrese numero entre 0 - 9 : "))

while True:

    if numero >= 1 and numero <= 9 and numero in lista:
        numero = int(input("El numero SI esta en la lista ingrese otro :"))
    elif numero >= 1 and numero <= 9 and numero not in lista:
        numero = int(input("El numero NO esta en la lista ingrese otro :"))
    else:
        numero = int(input("numero no valido ingrese del 0 - 9 : "))

else:
    pass







#6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

#Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

lista1 = list(range(0,11))

print(" todos los números del 0 al 10 \n",lista1)

lista2 = list(range(-10,1))

print("Todos los números del -10 al 0 \n",lista2)

lista3 = list(range(0,11,2))

print("Todos los números pares del 0 al 20 \n",lista3)

lista4 = list(range(-19,0,2))

print("Todos los números impares entre -20 y 0\n",lista4)

lista5 = list(range(0,51,5))

print("Todos los números múltiples de 5 del 0 al 50\n",lista5)



#6) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
# pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []

for item in lista_1:
    if item in lista_2 and item not in lista_3:
        lista_3.append(item)

print(lista_3)

