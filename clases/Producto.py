class Producto:
    def __init__(self, name, product_type, price):
        self.name = name
        self.product_type = product_type
        self.price = price

    def __str__(self):
        return f"Nombre: {self.name}, Tipo: {self.product_type}, Precio: {self.price}"
