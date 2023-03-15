import requests
import json
import uuid
from clases.Cliente import Cliente

class Venta_entradas:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        self.carreras = self.cargar_carreras()

    def cargar_carreras(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                carreras = json.loads(response.text)
                return carreras
            else:
                print("Error al obtener carreras desde la API")
                return []
        except Exception as e:
            print("Error al cargar carreras:", e)
            return []
    def cargar_asientos_disponibles(self, carrera):
        try:
            with open(f"datos/asientos_{carrera}.txt", "r") as archivo_asientos:
                asientos_ocupados = archivo_asientos.read().splitlines()
                asientos_ocupados = [tuple(map(int, asiento.split(','))) for asiento in asientos_ocupados]
                return asientos_ocupados
        except FileNotFoundError:
            return []
        
        
    def registrar_asiento(self, carrera, fila, asiento):
        with open(f"datos/asientos_{carrera}.txt", "a") as archivo_asientos:
            archivo_asientos.write(f"{fila},{asiento}\n")
    def mostrar_carreras(self):
        for i, carrera in enumerate(self.carreras):
            print(f"{i + 1}. {carrera['name']} - {carrera['date']} - {carrera['circuit']['name']}")
    
    def mostrar_asientos_disponibles(self, carrera, tipo_entrada):
        filas, columnas = self.carreras[carrera]['map'][tipo_entrada]
        asientos_ocupados = self.cargar_asientos_disponibles(self.carreras[carrera]['name'])

        print(f"Asientos disponibles para la entrada {tipo_entrada}:")
        for i in range(filas):
            for j in range(columnas):
                if (i, j) not in asientos_ocupados:
                    print(f"[{i + 1},{j + 1}]", end=" ")
                else:
                    print("[X]", end=" ")
            print()

    def obtener_datos_cliente(self):
        nombre = input("Ingrese su nombre: ")

        while True:
            try:
                cedula = int(input("Ingrese su cédula: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico para la cédula.")

        while True:
            try:
                edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico para la edad.")

        return Cliente(nombre, cedula, edad)


    def es_numero_ondulado(self, num):
        prev = num % 10
        num = num // 10
        es_par = prev % 2 == 0
        while num > 0:
            digito = num % 10
            if (digito % 2 == 0) == es_par:
                return False
            es_par = not es_par
            prev = digito
            num = num // 10
        return True

    def calcular_costo_entrada(self, tipo_entrada, cedula):
        precio_base = 150 if tipo_entrada == "general" else 340
        descuento = 0.5 if self.es_numero_ondulado(int(cedula)) else 1
        subtotal = precio_base * descuento
        iva = subtotal * 0.16
        total = subtotal + iva
        return subtotal, descuento, iva, total

    def guardar_venta(self, venta_info):
        try:
            with open("datos/ventas.txt", "a") as archivo_ventas:
                archivo_ventas.write(venta_info + "\n")
        except Exception as e:
            print("Error al guardar la venta:", e)

    def guardar_token(self, token_info):
        try:
            with open("datos/tokens.txt", "a") as archivo_tokens:
                archivo_tokens.write(token_info + "\n")
        except Exception as e:
            print("Error al guardar el token:", e)
    def generar_token(self):
        return str(uuid.uuid4())
    
    
    def start(self):
       
        cliente = self.obtener_datos_cliente()
        self.mostrar_carreras()
        
        
       
       
       
       
       
       
       
       
        numero_carreras = len(self.carreras)
        carrera_menu=True
        while carrera_menu:
            try:
                carrera_seleccionada = int(input(f"Seleccione el número de la carrera a la que desea comprar un ticket (1-{numero_carreras}): ")) - 1
                if 0 <= carrera_seleccionada < numero_carreras:
                    carrera_menu=False
                else:
                    print(f"Por favor, ingrese un número entre 1 y {numero_carreras}.")
            except ValueError:
                print("Por favor, ingrese un valor numérico.")
        tipo_entrada = input("Ingrese el tipo de entrada que desea comprar (general/vip): ").lower()
        self.mostrar_asientos_disponibles(carrera_seleccionada, tipo_entrada)
       
       
       
       
       
        menu_fila=True
        while menu_fila:
            try:
                fila = int(input("Ingrese el número de fila del asiento que desea comprar: ")) - 1
                menu_fila = False
            except ValueError:
                print("Por favor, ingrese un valor numérico.")
        menu_asiento=True
        while menu_asiento:
            try:
                asiento = int(input("Ingrese el número de asiento que desea comprar: ")) - 1
                menu_asiento=False
            except ValueError:
                print("Por favor, ingrese un valor numérico.")

        self.registrar_asiento(self.carreras[carrera_seleccionada]['name'], fila, asiento)
        
        # Aquí puedes implementar la selección de asientos y la generación del token

        subtotal, descuento, iva, total = self.calcular_costo_entrada(tipo_entrada, cliente.cedula)
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento: ${subtotal * (1 - descuento):.2f}")
        print(f"IVA: ${iva:.2f}")
        print(f"Total: ${total:.2f}")

        confirmar_compra = input("¿Desea proceder a pagar la entrada? (S/N): ").lower()
        if confirmar_compra == 's':
            # Aquí puedes implementar la ocupación del asiento
            
            

            token = self.generar_token()

            venta_info = f"{cliente.nombre},{cliente.cedula},{cliente.edad},{self.carreras[carrera_seleccionada]['name']},{tipo_entrada},{total}"
            self.guardar_venta(venta_info)

            token_info = f"{token},{cliente.nombre},{cliente.cedula},{self.carreras[carrera_seleccionada]['name']},{tipo_entrada},{total}"
            self.guardar_token(token_info)

            print("Pago exitoso.")
        else:
            print("Compra cancelada.")
