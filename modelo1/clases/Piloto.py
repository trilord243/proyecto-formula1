class Piloto:
    def __init__(self, nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.numero = numero
        self.constructor = None

    def asignar_constructor(self, constructor):
        self.constructor = constructor
