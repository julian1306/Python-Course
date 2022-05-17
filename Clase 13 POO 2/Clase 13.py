class Perro():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad #------------------con esto encapsulo la info , no se ve de afuera

    def mas_de_10(self):
        return self.edad > 18 #------------------con esto encapsulo la info , no se ve de afuera pero puedo operarlo

    def __str__(self):             # ------------ Hace que el nombre fiero del print(perro_1) . caundo llamo al objeto en si
        return f'El perro de  se llama {self.nombre}'

    def __len__(self): # ------------------------ pa que funcione el len en los objetos
        return len(self.nombre)    #--- te devuelve el len del nombre



class Persona:

    def __init__(self, nombre, apellido, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota

    def leer_apellido(self):
        print(self.apellido)

    #def __getitem__(self, item): -------- con este te pasa el item /posicion del nombre
        #return self.nombre[item]

    def __getitem__(self, pos):  # --------- con esto le digo que lea y me devuelva el item del parametro mascota
        return self.mascota[pos]

    def __setitem__(self, key, value):
        self.mascota[key] = value





    # def __str__(self):
    #     return "Mi nombre es: " +self.nombre +" " +self.apellido +"\n" +self.perro.__str__()





perro_1 = Perro('firulais', 15)
perro_2 = Perro('pepe', 10)
perro_3 = Perro ("negri", 15)

print(perro_1)
print(perro_2)

print(len(perro_1))

persona_1 = Persona('Gaston', "Roson", [perro_1, perro_2]) # ACA le paso como item mascota el perro1 y perro 2 que a su vez son
                                                            #otros objetos de la case perro

persona_2 = Persona('julian', "garcia", perro_3)


#GET ITEM
print(persona_1[0])
print(persona_1.mascota[0])

#get item le cambio el item de mascota en pos 0 por "negri"
persona_1[0] = "negri"

print(persona_1.mascota[0])

print(persona_2.mascota.edad) # ---------- edad de la mascota de persona 2

#----------------

class User():
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.__contraseña = contraseña # ----------------------- __ Encapsular oculta los datos fuera de la clase

    def validar_contraseña(self, contraseña):
        if self.__contraseña == contraseña:
            print('La contraseña es correcta')
        else:
            print('La contraseña es incorrecta')


usuario_1 = User('luca', '123123')

print("nombre del usuario 1 ", usuario_1.nombre) # ---------------- funciona porque no esta encapsulado
# print (usuario_1.contraseña) # -------------------------------- no funciona porque esta encapsulado con el __

for i in range(0, 3):
    password = input('ingrese su contraseña: ')
    usuario_1.validar_contraseña(password)
else:
    print('Te quedaste sin intentos')