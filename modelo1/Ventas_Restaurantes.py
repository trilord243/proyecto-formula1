import requests

class Ventas_Restaurantes:

    def __init__(self):
        self.inventario = {}  # Para almacenar el inventario de productos
        self.clientes = {}  # Para almacenar los datos de los clientes
        self.clientes_edad = {}  # Para almacenar la edad de los clientes según su cédula
        self.ventas = []  # Para almacenar las ventas realizadas
        self.API_URL = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        self.races_data = []

    def cargar_datos(self):
        # Cargar datos de la API
        response = requests.get(self.API_URL)
        self.races_data = response.json()
        for race in self.races_data:
            for restaurant in race["restaurants"]:
                self.inventario[restaurant["name"]] = restaurant["items"]

        # Cargar datos de tokens.txt
        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(",")
                cedula = campos[2]
                tipo_entrada = campos[4]
                self.clientes[cedula] = tipo_entrada

        # Cargar datos de ventas.txt
        with open("datos/ventas.txt", "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(",")
                cedula = campos[1]
                edad = int(campos[2])
                self.clientes_edad[cedula] = edad

    def obtener_carrera_cliente(self, cedula):
        with open("datos/ventas.txt", "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(",")
                cedula_ventas = campos[1]
                carrera = campos[3]
                if cedula_ventas == cedula:
                    return carrera
        return None
    def es_cliente_vip(self, cedula):
        return self.clientes.get(cedula) == "vip"
    
    def mostrar_productos_disponibles(self, carrera_cliente):
        self.productos_numerados = {}
        indice = 1
        for race in self.races_data:
            if race["name"] == carrera_cliente:
                print("\nProductos disponibles en la carrera {}:".format(carrera_cliente))
                for restaurant in race["restaurants"]:
                    print("\nRestaurante {}:".format(restaurant["name"]))
                    for item in restaurant["items"]:
                        print("{} - {} - ${}".format(indice, item["name"], item["price"]))
                        self.productos_numerados[indice] = item
                        indice += 1
    def realizar_compra(self, cedula, productos):
        if not self.es_cliente_vip(cedula):
            print("Lo sentimos, solo los clientes VIP pueden realizar compras en el restaurante.")
            return

        edad_cliente = self.clientes_edad.get(cedula)
        if edad_cliente is not None and edad_cliente < 18:
            productos = [p for p in productos if not (p["type"].startswith("drink") and "alcoholic" in p["type"])]

        subtotal = sum(float(p["price"]) for p in productos)
        descuento = (0.15 * subtotal) if self.es_numero_perfecto(int(cedula)) else 0
        total = subtotal - descuento

        self.mostrar_resumen_compra(cedula, productos, subtotal, descuento, total)
        self.guardar_venta(cedula, productos, total)
        return subtotal, descuento, total
    
    def mostrar_resumen_compra(self, cedula, productos,subtotal,descuento, total):
        print("\nResumen de compra:")
        print("Cédula del cliente: {}".format(cedula))
        print("Productos comprados:")
        for producto in productos:
            print(" - {}: ${}".format(producto["name"], producto["price"]))
        print("Subtotal: ${}".format(subtotal))  # Agregue esta línea
        print("Descuento: ${}".format(descuento))  # Agregue esta línea
        print("Total: ${}".format(total))
            
    

    def guardar_venta(self, cedula, productos,  total):
        carrera_cliente = self.obtener_carrera_cliente(cedula)
        with open("datos/ventas_realizadas.txt", "a") as ventas_file:
            for producto in productos:
                linea = f"{cedula},{producto['name']},{carrera_cliente},{producto['price']},{total}\n"
                ventas_file.write(linea)



    def es_numero_perfecto(self, num):
        sum_divisores = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                sum_divisores += i
        return sum_divisores == num

    def start(self):
        self.cargar_datos()
        menu_1=True
        while menu_1:
            print("Ingrese su cédula o 'salir' para terminar:")
            cedula = input().strip()

            if cedula.lower() == "salir":
                menu_1 = False

            carrera_cliente = self.obtener_carrera_cliente(cedula)
            if not self.es_cliente_vip(cedula):
                print("Lo sentimos, solo los clientes VIP pueden realizar compras en el restaurante.")
                continue

            productos = []
            menu_2=True
            while menu_2:
                self.mostrar_productos_disponibles(carrera_cliente)
                print("Ingrese el número del producto que desea comprar o 'terminar' para finalizar:")
                producto_numero = input().strip()

                if producto_numero.lower() == "terminar":
                    menu_2=False

                if producto_numero.isdigit():
                    producto_numero = int(producto_numero)
                    producto = self.productos_numerados.get(producto_numero)

                    if producto:
                        productos.append(producto)
                    else:
                        print("Producto no encontrado, por favor intente de nuevo.")
                else:
                    print("Entrada inválida, por favor ingrese un número.")

            compra = self.realizar_compra(cedula, productos)
            if compra:
                subtotal, descuento, total = compra
                self.mostrar_resumen_compra(cedula, productos, subtotal, descuento, total)

        print("Gracias por utilizar nuestra aplicación. ¡Hasta pronto!")
        

