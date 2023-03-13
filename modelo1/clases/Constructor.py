class Constructor:
    def __init__(self, id, nombre, nacionalidad,pilotos_ref):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.pilotos_ref = pilotos_ref
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.nacional} - {self.pilotos_ref}"  

    
