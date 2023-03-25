class Carrera:
    def __init__(self, nombre, numero, fecha, circuito,asientos=0, podium=[]):
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha
        self.circuito = circuito
        self.asientos = asientos
        self.podium = podium
        
    
    def guardar_datos(self):
        podium_str = ','.join([str(piloto_id) for piloto_id in self.podium])
        with open("datos/carreras.txt", "a") as archivo:
            archivo.write(f"{self.nombre},{self.numero},{self.fecha},{self.circuito},{podium_str}\n")
        
    def __str__(self):
        return f"Carrera {self.numero}: {self.nombre} - {self.fecha} en el circuito {self.circuito}"
    
    

