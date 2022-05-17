from clases import Auto
# Con esto creo archivo python aparte para estar mas ordenado donde tenga solo las clases
# y lo llamo con el  from import(nombre del archivo) y la clase

auto1 = Auto("alfa romeo","giulietta","negro", 230)
auto2 = Auto("VW","gol","azul",98)
auto3 = Auto("ford", "focus","blanco",140)

print("caracteristicas auto N1 :")
print(auto1.marca)
print(auto1.modelo)
print(auto1.color)
print(auto1.ruedas)

print("caracteristicas auto N2 :" )
print(auto2.marca)
print(auto2.modelo)
print(auto2.color)
print(auto2.ruedas)

#aca llamo al objeto auto en la funcion arrancar
print("auto N 1 : ")
auto1.arrancar()

print("auto N 2 : ")
auto2.arrancar()

print("velociudades : ")
auto1.velocidad()
auto2.velocidad()
auto3.velocidad()

##### Parametros defeto
#!!!!!!!!!print N 55 !!!!!!!!!!!!!
print("ruedas auto 1 : ")
print(auto1.ruedas)
# aca si quiero printear las ruedas de la clase total da error auto.ruedas
# AttributeError: type object 'auto' has no attribute 'ruedas' porque esta solo cuando se crea el obejeto no en la clase total


#print(auto.ruedas)



