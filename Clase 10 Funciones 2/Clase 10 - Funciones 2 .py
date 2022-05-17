
#Si le mando lista a el def me va  a modificar la lista , dic , set  a menos que haga un . copy al igualar a la nueva variable
def duplicar_numeros (numeros):
    numeros_funcion = numeros.copy() #---------------------------- ACA
    for indice in range(len(numeros_funcion)):
        numeros_funcion[indice] *=2
    return numeros_funcion


numeros = [5, 10, 20]

print("numeros antes funcion", numeros)
duplicar_numeros(numeros)
print("numeros despues funcion",numeros)



######################################################

# poner valor por defecto
def valor_defecto(valor = 10): # ------------------ con el valor =10 le digo por defecto que es 10 si no ingresa nada

    valor = valor + "10"
    return valor

valor = input("ingrese valor >" )
print(valor_defecto(valor))


##################################
# Cuando no se cuantos argumentos/valores me va a pasar en la funcion el HDP se le pone en ( *args) , haciendo esto lo guarda en una tupla
# por eso se tiene que usar el for

def suma(a, b, *args):
  suma = a + b
  for arg in args:
    suma += arg
  return suma

print(suma(5,10,10,10,10))

##################################################
#Le mando variables completas para eso se usa *kwargs las guarda como diccionario

def calculadora(*args, **kwargs):
  suma = 0
  if 'operacion' in kwargs:
    if kwargs['operacion'] == 'suma':
      for arg in args:
        suma += arg
    elif kwargs['operacion'] == 'resta':
      for arg in args:
        suma -= arg
  return suma


operacion = input('Ingrese la operacion a realizar (suma/resta): ')
print(calculadora(30, 100, 80, 30, 22, 5, operacion = operacion))


###############################################################
# FUNCIONES RECURSIVAS
import time

def cuenta(numero):
  numero -= 1
  if numero > 0:
    print('-------->', numero)
    time.sleep(1)
    cuenta(numero)
    print('ahora estoy volviendo')
  else:
    print('Ahhh, explotaste...')


# RECURSIVAS FACTORIAL


def factorial(numero):
  print("Valor inicial ->", numero)
  if numero > 1:
    numero = numero*factorial(numero -1)
  print("Valor final ->", numero)
  return numero


print(factorial(3))


