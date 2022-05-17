#diccionarios :


colores = {"amarillo": 'yellows', "azul": 'blue', "rojo": 'red', 'cantidad': 220, 'alumnos':{'alumno_1':'Agustin','alumno_2':'Arturo','alumno_3':'Jonathan'}, 10:'diez', 20:'veinte'}

#aca modifica por key el valor
colores['amarillo'] = 'yellow'

print(colores)

#aca busca dentro dic colores la key alumnos y dentro del dic alumnos busca la key alumno_3 osea devuelve jonathan
print(colores['alumnos']['alumno_3'])




# aca le hace un pop con la key
numeros =  {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
print(numeros.pop('uno'))

print(numeros)