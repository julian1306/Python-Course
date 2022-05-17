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
    except Exception as e:  # guardamos la excepción como una variable e
        print("Ha ocurrido un error =>", type(e).__name__)



a = input("ingrese num a dividir :")
b = input("ingrese num a dividir10 :")

dividir(a,b)