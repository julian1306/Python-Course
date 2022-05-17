# Ejercicio N1
def area_rectangulo(basein, alturain):
    resultado = basein * alturain
    return resultado



base = 15
altura = 10

print("El area del rectangulo es :", area_rectangulo(base, altura))


# Ejercicio N2
import math

def area_circulo(radioin):
    resultado = radioin ** 2 *math.pi
    return resultado


radio = 5

print("El area del circulo es :", area_circulo(radio))


# Ejercicio N3

def relacion(valor1, valor2):
    if valor1 > valor2:
        return 1
    elif valor1 < valor2:
        return -1
    elif valor1 == valor2:
        return 0

numero1 = 5
numero2 = 10
numero3 = 10
numero4 = 5
numero5 = 5
numero6 = 5

relacion_1 = relacion(numero1,numero2)
relacion_2 = relacion(numero3,numero4)
relacion_3 = relacion(numero5,numero6)

print("relacion N1 : ",relacion_1)
print("relacion N2 : ",relacion_2)
print("relacion N3 : ",relacion_3)


# Ejercicio 4

def intermedio(numero1,numero2):
    promedio = (numero1 + numero2)/2
    return promedio

numero_intermedio1 = -12
numero_intermedio2 = 24

promedio = intermedio(numero_intermedio1,numero_intermedio2)

print("Numero intermedio es : ", promedio)

# Ejercicio 5

def recortar(numero_arecortar,limite_inferior,limite_superior):
    if numero_arecortar < limite_inferior:
        return limite_inferior
    elif numero_arecortar > limite_superior:
        return  limite_superior
    else:
        return  numero_arecortar

numero = 15
inferior = 0
superior = 10

recorte = recortar(numero,inferior,superior)

print("el recorte es : ", recorte)

# Ejercicio 6


def separar(lista):

    pares = []
    impares = []
    for list in lista:
        if list % 2 == 0:
            pares.append(list)
            pares.sort()
        else:
            impares.append(list)
            impares.sort()
    print("Estos son los pares :",pares)
    print("Eston son los impares :",impares)



lista = [6,5,2,1,7]
resultado= separar(lista)



