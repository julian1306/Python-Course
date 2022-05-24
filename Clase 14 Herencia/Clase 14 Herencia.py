# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass


class Animal:

  def __init__(self, especie, edad):#Constructor como siempre en la clase Padre
    self.especie = especie
    self.edad = edad

  def hablar(self):  #Método generico vacio por ahora
    pass

  def moverse(self): #Método generico vacio por ahora
    pass

  def __str__(self):
    return f"ESPECIE: {self.especie} , EDAD: {self.edad}"

  def describir(self):  #Método con una implementación
    print(f"Soy un animal del tipo: {type(self).__name__}")

animal_1 = Animal('mono', 15)
animal_1.describir()


class Perro(Animal):

  def hablar(self):  # Modifica el método generico y lo trabaja a su forma
    print("Guau!")

  def moverse(self):  # Lo mismo para este otro método
    print("Caminando con 4 patas")


perro1 = Perro("Mamífero", 11)  #INCREIBLE, cree un perro y la clase perro no
#tiene atributos, solo los heredo de su padre.
print (perro1)

perro1.hablar()
perro1.moverse()


class Vaca(Animal):
  def hablar(self):
    print("Muuu!")

  def moverse(self):
    print("Caminando con 4 patas")


class Abeja(Animal):
  def hablar(self):
    print("Bzzzz!")

  def moverse(self):
    print("Volando")

  # Nuevo método
  def picar(self):
    print("Picar!")



####

class Perro(Animal):
  def __init__(self, especie, edad, duenio):  # --------- 1) Podemos crear un nuevo init y guardar todas las variables una a una.
      # Alternativa 1
      # self.especie = especie
      # self.edad = edad
      # self.dueño = dueño

      # Alternativa 2 ------------------O podemos usar super() para llamar al init de la clase padre que ya aceptaba la especie y edad,
    #                                     y sólo asignar la variable nueva manualmente
    super().__init__(especie, edad)
    self.duenio = duenio


mi_perro = Perro("mamifero", 7 ,"luis") # Aca creo perro con especie y edad como en clase madre animal . y le agrego la nueva duenio




