
# Ejercicio 4
numero_1 = 9
numero_2 = 3
numero_3 = 6

prom1 = int(15)
prom2 = int(35)
prom3 = int(50)

print("Ejercicio 4", "\n" , "Promedio :" , (numero_1*prom1 + numero_2*prom2 + numero_3*prom3) / (prom1+prom2+prom3))



#EJERCICIO 5

matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

suma0 = sum(matriz[0])
suma1 = sum(matriz[1])
suma2 = sum(matriz[2])
suma3 = sum(matriz[3])

matriz[0].append(suma0)
matriz[1].append(suma1)
matriz[2].append(suma2)
matriz[3].append(suma3)

print("Ejercicio 5 : ", "\n" ,matriz [0],"\n", matriz [1],"\n", matriz [2],"\n", matriz [3])
