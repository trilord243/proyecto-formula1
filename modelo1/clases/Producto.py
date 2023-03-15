class Producto:
    def __init__(self, nombre, clasificacion, precio, es_alcoholica=None, es_empaque=None):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.precio = precio * 1.16
        self.es_alcoholica = es_alcoholica
        self.es_empaque = es_empaque