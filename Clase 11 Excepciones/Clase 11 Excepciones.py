# Try and except Aca lo obligo a que si tira error por no poner un float le manda mensaje y vuelve por el while

while True:
    try:
        n = float(input("ingrese numero N1 : "))
        m = float(input("ingrese numero N2 : "))
        print(f"resultado : {n}+{m} = {n+m}")
        break
    except:
        print("Error Ingrese un numero ")

