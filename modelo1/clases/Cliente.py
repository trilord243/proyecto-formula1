class Cliente:
    def __init__(self, nombre, cedula, edad, carrera_numero, tipo_entrada, fila):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.carrera_numero = carrera_numero
        self.tipo_entrada = tipo_entrada
        self.fila = fila

    def __str__(self):
        return f"{self.nombre}, {self.cedula}, {self.edad}, {self.carrera_numero}, {self.tipo_entrada}, {self.fila}"