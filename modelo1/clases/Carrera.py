class Carrera:
    def __init__(self, nombre, numero, fecha, circuito, podium):
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha
        self.circuito = circuito
        self.podium = podium
    def asignar_piloto_podium(self, piloto, posicion):
        self.podium.append((piloto, posicion))
