class Constructor:
    def __init__(self, id, nombre, nacionalidad):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.pilotos = []

    def agregar_piloto(self, piloto):
        self.pilotos.append(piloto)
