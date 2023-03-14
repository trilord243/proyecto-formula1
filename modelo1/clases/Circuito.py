class Circuito:
    def __init__(self, nombre, pais, localidad, latitud_longitud):
        self.nombre = nombre
        self.pais = pais
        self.localidad = localidad
        self.latitud_longitud = latitud_longitud
    
    def __str__(self):
        return self.nombre + " " + self.pais + " " + self.localidad + " "