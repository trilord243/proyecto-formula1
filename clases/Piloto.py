class Piloto:
    def __init__(self, nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero,id):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.numero = numero
        self.id = id
        self.puntos=0

    
    def agregar_puntos(self, puntos):
        self.puntos += puntos
    
    
    def guardar_datos(self):
        with open("datos/pilotos.txt", "a") as archivo:
            archivo.write(f"{self.nombre},{self.apellido},{self.fecha_nacimiento},{self.lugar_nacimiento},{self.numero},{self.id},{self.puntos}\n")