
animales= {'elefante': ''}

animales.update({'perro':'bobby','tigre':'peepe', 'mono':'homero'})
#print(animales)

#animales['elefante']='trompis'
animales['delfin']='manolo'

#print(animales)

#key:valus
frutas = {'rojo':'manzana','verde':'pera' ,'amarillo':'banana'}
#########################
#FOR en diccionario
#para recorrer los valores

for frut in frutas.keys():
    print("keys: ",frut)

for frut2 in frutas.values():
    print("Valores",frut2)

#metodos keys y values
print(frutas.keys())
print(frutas.values())


