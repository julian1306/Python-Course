# Try and except Aca lo obligo a que si tira error por no poner un float le manda mensaje y vuelve por el while
#ACA con un else . si se cumple el try pasa al else, en cambio si se hace el excep no
#Finally se ejecuta si o si . se rompa , salga por el excel o por el else .

while True:
    try:
        n = float(input("ingrese numero N1 : "))
        m = float(input("ingrese numero N2 : "))
        print(f"resultado suma : {n}+{m} = {n + m}")


    except:
        print("Error Ingrese un numero ")
    else:
        print("perfecto la suma funciono ")
        print(f"este es el resultado de la resta : {n}-{m} = {n-m}")
        break
    finally:
        print("Finalizo correctamente")


#Excepciones as

try:
  n = int(input("Introduce un número: "))  # no transformamos a número
  division = n/5
  print("division :", division)
except Exception as e:  # guardamos la excepción como una variable e
  print("Ha ocurrido un error =>", type(e).__name__)

#excepcion 2


def dividir(a, b):
    try:
        a = int(a)
        b = int(b)
        return a/b

    except ZeroDivisionError:
        print('division x 0')
    except ValueError:
        print('algo no es un nro')
    except TypeError:
        print('algo no es un nro')



a = input("ingrese num a dividir :")
b = input("ingrese num a dividir10 :")

dividir(a,b)