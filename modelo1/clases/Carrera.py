class Carrera:
    def __init__(self, nombre, numero, fecha, circuito, podium):
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha
        self.circuito = circuito
        self.podium = podium
    def __str__(self):
        return self.nombre + " " + self.numero + " " + self.fecha + " "+ self.circuito + " " + self.podium
        
