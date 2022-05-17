ruta = 'C:/Users/julian/Desktop/Curso python/Clase 8/'

f = open(ruta + 'prueba.txt', 'w')

f.write("prueba texto")

f.close()

#----------------------------------


nombre = "julian"
apellido = "garcia"
dni = 38526314
nacionalidad = 'Argentino'


data = {"nombre":nombre, "apellido":apellido, "DNI":dni, "nacionalidad":nacionalidad}

f = open(ruta + "/texto_datos.txt", "w")

f.write(data["nombre"]+ ","+ data["apellido"] + "," + str(data["DNI"]) + "," + data["nacionalidad"])

f.close()


##################################

f = open(ruta + "/paraLeer.txt", "r")

content = f.read()

print(content)

f.close()

############################


f = open(ruta + "/paraLeer.txt", "r")

#si sacas el # aca lo hace como una lista
#print("Este es read lines : ",f.readlines())



#aca con un for como si fuera una lista
for line in f.readlines():
    print(line)

f.close()

######################################

f = open(ruta + "/paraLeer.txt", "r")

print("solo red line   : " , f.readline())

f.close()

##########################################

f = open(ruta + "/paraLeer.txt", "r")

f.seek(21)

print("este el seek : " , f.read())

f.close()

###################################
#importa las funciones de json

import json

data = {}

data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

with open(ruta + "/primerJson.json", 'w') as file:
    json.dump(data, file)

##############
#imprime lo de la info que cargamos arriba del json

with open(ruta + "/primerJson.json") as file:

    dataLectura = json.load(file)

    for client in dataLectura['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')


#######################################################

#Para generar una variable con los datos de nuestro archivos, vamos a empezar a trabajar con nuestra libreria "magica" para trabajar con datos,
#libreria llamada Pandas, para poder usarla debemos hacer lo siguiente

import pandas as pd

#En castellano, importamos pandas y lo llamamos pd  (pd puede ser cualquier palabra que recuerden)


variableTurnos = pd.read_csv(ruta + "/dataset_turnos_detalle.csv")
#datos.to_csv('datosAPPL.csv')


print(variableTurnos)

#######################################################


#Si esa visualización por defecto no nos gusta podemos verlos de otra forma. Head, nos permite elegir cuantos datos mostrar
print(variableTurnos.head(10)) #Los primeros


#Con el comando tails, agarramos los ultimos
print(variableTurnos.tail(10))


#Tambien podemos usar sample, que nos muestra la cantidad que quieras, pero al azar, bastante util.
print(variableTurnos.sample(10))

print(variableTurnos.describe())


#Uno de los primeros estadisticos para entrar en tema podría ser las frecuencias simples..
print(variableTurnos['sede'].value_counts())  #Esto nos muestra cada sede una vez sola, ordenado y con su frecuencia.