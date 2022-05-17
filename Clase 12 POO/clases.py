#aca se crea el objeto auto con el contructor __init__ . y se le dan atributos por parametro color , marca
class Auto():
    # ruedas = 4     # parametro por defecto en clase global de autos todos , ver en print N55 si definis aca asi si funciona el print(auto.ruedas)

    def __init__(self,marca, modelo , color, potencia):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.ruedas = 4   #----------------------------------- si la defino aca solo es cuando se crea el obejto ver print N55

    def arrancar(self):
        print(f"el {self.marca} {self.modelo} {self.color} acaba de arrancar")

    def velocidad(self):
        if self.potencia <= 100:
            print(f"el {self.marca} {self.modelo} es lento")
        elif self.potencia > 100 and self.potencia <= 160:
            print (f"el {self.marca} {self.modelo} es medianamente rapido")
        elif self.potencia > 160:
            print(f"el {self.marca} {self.modelo} es rapido")
