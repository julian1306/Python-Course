class Celular_gama_baja():
    def __init__(self, modelo, precio, memoria, calidad_fotos):
        self.modelo = modelo
        self.precio = precio
        self.memoria = memoria
        self.calidad_fotos = calidad_fotos

    def sacar_fotos(self):
        print(f'El celular saco una foto con {self.calidad_fotos}')
    
    def __str__(self):
        return f'\nModelo: {self.modelo}\n\nPrecio: {self.precio}\nMemoria:{self.memoria}\nCalidad fotos: {self.calidad_fotos}'

class Celular_gama_media(Celular_gama_baja):
    def __init__(self, modelo, precio, memoria, calidad_fotos, calidad_videos):
        super().__init__(modelo, precio, memoria, calidad_fotos)
        self.calidad_videos = calidad_videos

    def grabar_tiktoks(self):
        print(f'Estamos grabando tiktocks para hacernos famosos en {self.calidad_videos}')

    def __str__(self):
        return f'\nModelo: {self.modelo}\n\nPrecio: {self.precio}\nMemoria:{self.memoria}\nCalidad fotos: {self.calidad_fotos}\nCalidad videos: {self.calidad_videos}'

class Celular_gama_alta(Celular_gama_media):
    def __init__(self, modelo, precio, memoria, calidad_fotos, calidad_videos, calidad_fotos_2):
        super().__init__(modelo, precio, memoria, calidad_fotos, calidad_videos)
        self.calidad_fotos_2 = calidad_fotos_2

    def sacar_fotos(self):
        print(f'El celular saco una foto con la camara principal de {self.calidad_fotos}')
    
    def sacar_fotos_secundaria(self):
        print(f'El celular saco una foto con la camara secundaria de {self.calidad_fotos_2}')

    def __str__(self):
        return f'\nModelo: {self.modelo}\n\nPrecio: {self.precio}\nMemoria:{self.memoria}\nCalidad fotos principal: {self.calidad_fotos}\nCalidad fotos secundaria: {self.calidad_fotos_2}\nCalidad videos: {self.calidad_videos}'
