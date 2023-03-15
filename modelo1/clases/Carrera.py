class Carrera:
    def __init__(self, nombre, numero, fecha, circuito, podium=[]):
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha
        self.circuito = circuito
        self.podium = podium
    
    def guardar_datos(self):
        podium_str = ','.join([str(piloto_id) for piloto_id in self.podium])
        with open("carreras.txt", "a") as archivo:
            archivo.write(f"{self.nombre},{self.numero},{self.fecha},{self.circuito},{podium_str}\n")
        
    
    
    

