class Piloto:
    def __init__(self, nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero,id):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.numero = numero
        self.id = id

    def asignar_constructor(self, constructor):
        self.constructor = constructor
