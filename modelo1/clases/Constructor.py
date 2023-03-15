class Constructor:
    def __init__(self, id, nombre, nacionalidad,pilotos_ref):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.pilotos_ref = pilotos_ref
        self.puntos=0
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.nacional} - {self.pilotos_ref}"  

    
    def agregar_puntos(self, puntos):
        self.puntos += puntos
    
    def guardar_datos(self):
        with open("constructor_with_points.txt", "a") as archivo:
            archivo.write(f"{self.nombre},{self.id},{self.nacionalidad},{self.pilotos_ref[0]},{self.pilotos_ref[1]},{self.puntos}\n")