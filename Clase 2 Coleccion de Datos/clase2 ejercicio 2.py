
#defino la tupla
tupla = (5,12,7,37,8,86,19,7,-783,87,188,7,9,12,7,3982)

#printeo la tupla con slincing del ultimo -1
print("1. El ultimo item de la tupla : ", tupla [-1])

#printeo len para contar los items de la tupla
print("2. El numero de items de la tupla :", len(tupla))

#printeo la tupla con el .index me busca la posicion que tenga el 87
print("3. La posicion donde se encuentra el item 87 de la tupla: ", tupla.index(87))

#creo la lista 1 con los ultimos 3 de la tupla
lista1 = [tupla[-3:]]

#printeo lo de arriba
print("4. Una lista con los ultimos tres items de tupla : ", lista1 )




print("5. Un item que haya en la posicion 8 de la tupla : ", tupla [-8])


# llamo a la tupla pongo punto tupla. el comando count y el numero en cuestion
print(" 6. -el numero de veces que el item 7 aparece en tupla : ",  tupla.count(7))







