class Carrera:
    def __init__(self, nombre, numero, fecha, circuito):
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha
        self.circuito = circuito
        
    def __str__(self):
        return self.nombre + " " + self.numero + " " + self.fecha + " "+ self.circuito + " " 
        
