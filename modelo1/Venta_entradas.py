import requests
import json
import uuid
from clases.Cliente import Cliente

class Venta_entradas:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        self.carreras = self.cargar_carreras()


    def cargar_carreras(self):
        response = requests.get(self.url)
        carreras = json.loads(response.text)
        return carreras
                    


    def cargar_asientos_disponibles(self, carrera):
        try:
            with open(f"datos/asientos_{carrera}.txt", "r") as archivo_asientos:
                asientos_ocupados = archivo_asientos.read().splitlines()
                asientos_ocupados = [tuple(map(int, asiento.split(','))) for asiento in asientos_ocupados]
                return asientos_ocupados
        except FileNotFoundError:
            return []
        
    
    
    
    def asiento_disponible(self, carrera, fila, asiento):
        asientos_ocupados = self.cargar_asientos_disponibles(carrera)
        return (fila, asiento) not in asientos_ocupados
    
    def asiento_en_rango(self, carrera, fila, asiento, tipo_entrada):
        filas, columnas = self.carreras[carrera]['map'][tipo_entrada]
        return 0 <= fila < filas and 0 <= asiento < columnas
   
    
    
        
        
    def registrar_asiento(self, carrera, fila, asiento):
        with open(f"datos/asientos_{carrera}.txt", "a") as archivo_asientos:
            archivo_asientos.write(f"{fila},{asiento}\n")
    def mostrar_carreras(self):
        for i, carrera in enumerate(self.carreras):
            print(f"{i + 1}. {carrera['name']} - {carrera['date']} - {carrera['circuit']['name']}")
    
    
    def todos_asientos_ocupados(self, carrera, tipo_entrada):
        filas, columnas = self.carreras[carrera]['map'][tipo_entrada]
        asientos_totales = filas * columnas
        asientos_ocupados = len(self.cargar_asientos_disponibles(self.carreras[carrera]['name']))
        
        return asientos_ocupados >= asientos_totales

    
    def mostrar_asientos_disponibles(self, carrera, tipo_entrada):
        if self.todos_asientos_ocupados(carrera, tipo_entrada):
            return 

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
        dato_menu1=True
        while dato_menu1:
            try:
                cedula = int(input("Ingrese su cédula: "))
                dato_menu1=False
            except ValueError:
                print("Por favor, ingrese un valor numérico para la cédula.")
        dato_menu2=True
        while dato_menu2:
            try:
                edad = int(input("Ingrese su edad: "))
                dato_menu2=False
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
                archivo_tokens.write(token_info + ",Asistirá\n")  # Agregar ",Asistirá" al final de la línea
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
        
        tipo_menu=True
        while tipo_menu:
            tipo_entrada = input("Ingrese el tipo de entrada que desea comprar (general/vip): ").lower()
            if tipo_entrada == "vip" or tipo_entrada == "general":
                tipo_menu=False
            else:
                print("Por favor, ingrese 'general' o 'vip'.")
        self.mostrar_asientos_disponibles(carrera_seleccionada, tipo_entrada)
        cerrar_menu = self.todos_asientos_ocupados(carrera_seleccionada, tipo_entrada)
        
        if cerrar_menu:
            print("No hay asientos disponibles, saliendo del menú.")
        else:
            asiento_disponible = False
            
        
            while not asiento_disponible:
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
                    
                if self.asiento_en_rango(carrera_seleccionada, fila, asiento, tipo_entrada):
                    if self.asiento_disponible(self.carreras[carrera_seleccionada]['name'], fila, asiento):
                        asiento_disponible = True
                    else:
                        print("El asiento seleccionado no está disponible. Por favor, elija otro asiento.")
                        self.mostrar_asientos_disponibles(carrera_seleccionada, tipo_entrada)
                else:
                    print("El asiento seleccionado no está dentro del rango permitido. Por favor, elija otro asiento.")
                    self.mostrar_asientos_disponibles(carrera_seleccionada, tipo_entrada)


            self.registrar_asiento(self.carreras[carrera_seleccionada]['name'], fila, asiento)
            
            # Aquí puedes implementar la selección de asientos y la generación del token

            subtotal, descuento, iva, total = self.calcular_costo_entrada(tipo_entrada, cliente.cedula)
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Descuento: ${subtotal * (1 - descuento):.2f}")
            print(f"IVA: ${iva:.2f}")
            print(f"Total: ${total:.2f}")

            confirmar_compra = input("¿Desea proceder a pagar la entrada? (S/N): ").lower()
            if confirmar_compra == 's':
                token = self.generar_token()

                venta_info = f"{cliente.nombre},{cliente.cedula},{cliente.edad},{self.carreras[carrera_seleccionada]['name']},{tipo_entrada},{total}"
                self.guardar_venta(venta_info)

                token_info = f"{token},{cliente.nombre},{cliente.cedula},{self.carreras[carrera_seleccionada]['name']},{tipo_entrada},{total}"
                self.guardar_token(token_info)

                print("Pago exitoso.")
                print(f"Su token de entrada es: {token}")  # Muestra el token al cliente
            else:
                print("Compra cancelada.")