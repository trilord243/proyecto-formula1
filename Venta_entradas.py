import requests
import random
from clases.Cliente import Cliente
from clases.Entrada import Entrada
from clases.Sala import Sala
from clases.Asiento import Asiento
from clases.Carrera import Carrera
response = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json")
carreras_api = response.json()
class Venta_entradas:
    def __init__(self):
        self.carreras = []
        self.sala = Sala()  # Crear una instancia de la clase Sala
        self.cargar_carreras()


    def cargar_carreras(self):
        for carrera_api in carreras_api:
            nombre = carrera_api["name"]
            numero = int(carrera_api["round"])
            fecha = carrera_api["date"]
            circuito = carrera_api["circuit"]["circuitId"]
            carrera = Carrera(nombre, numero, fecha, circuito)
            self.carreras.append(carrera)

    def cargar_asientos_txt(self):
        asientos = []
        try:
            with open("datos/asientos.txt", "r") as file:
                for fila, line in enumerate(file):
                    fila_asientos = []
                    for columna, estado in enumerate(line.strip()):
                        fila_asientos.append(estado == "L")
                    asientos.append(fila_asientos)
        except FileNotFoundError:
            print("Archivo de asientos no encontrado. Se creará uno nuevo.")
            self.crear_archivo_asientos_vacios()  # Crear archivo de asientos vacíos si no existe
            asientos = self.cargar_asientos_txt()  # Intentar cargar de nuevo el archivo recién creado
        return asientos
    
    

    def mostrar_asientos(self):
        self.sala.mostrar_asientos()

            
            
    def guardar_asientos_txt(self):
        with open("datos/asientos.txt", "w") as file:
            for fila in range(len(self.sala.asientos)):
                for columna in range(len(self.sala.asientos[fila])):
                    file.write("D" if not self.sala.asientos[fila][columna] else "L")
                file.write("\n")

    


            
    def guardar_cliente_token(self, cliente, token):
        with open("datos/cliente_tokens.txt", "a") as archivo:
            archivo.write(f"{cliente.cedula},{token}\n")

    def mostrar_carreras(self):
        for carrera in self.carreras:
            print(carrera)

    def preguntar_datos_cliente(self):
        nombre = input("Nombre del cliente: ")
        cedula = input("Cedula: ")
        edad = int(input("Edad: "))
        self.mostrar_carreras()
        carrera_numero = int(input("Número de la carrera a la que desea comprar ticket: "))
        tipo_entrada = input("Tipo de entrada que desea comprar (General/VIP): ")
        fila = int(input("Seleccione la fila (1-10): "))
        return Cliente(nombre, cedula, edad, carrera_numero, tipo_entrada, fila)


    
    def vender_entrada(self, cliente):
        # Seleccionar carrera
        carrera_seleccionada = None
        for carrera in self.carreras:
            if carrera.numero == cliente.carrera_numero:
                carrera_seleccionada = carrera
                break

        # Asignar asiento disponible en la fila elegida
        asiento_fila = cliente.fila
        asiento_columna = random.randint(1, 10)
        while carrera_seleccionada.asientos[asiento_fila - 1][asiento_columna - 1]:  # Si el asiento no está disponible, buscar otro en la misma fila
            asiento_columna = random.randint(1, 10)

        carrera_seleccionada.asientos[asiento_fila - 1][asiento_columna - 1] = True  # Marcar el asiento como no disponible
        self.guardar_asientos_txt()  # Actualizar el archivo de asientos
        asiento = Asiento(asiento_fila, asiento_columna)
        entrada = Entrada(cliente, carrera_seleccionada, asiento, cliente.tipo_entrada)

        return entrada



    def es_numero_ondulado(self, numero):
        numero = str(numero)
        for i in range(1, len(numero) - 1):
            if int(numero[i]) == (int(numero[i - 1]) + int(numero[i + 1])) / 2:
                return True
        return False

    def calcular_costo_entrada(self, entrada):
        costo_base = 150 if entrada.tipo_entrada == "General" else 340
        subtotal = costo_base

        if self.es_numero_ondulado(entrada.cliente.cedula):
            descuento = costo_base * 0.5
        else:
            descuento = 0

        subtotal -= descuento
        iva = subtotal * 0.16
        total = subtotal + iva

        return subtotal, descuento, iva, total

    def confirmar_pago(self, entrada, subtotal, descuento, iva, total):
        print("\nResumen de compra:")
        print("Asiento:", entrada.asiento)
        print("Subtotal: ${:.2f}".format(subtotal))
        print("Descuento: ${:.2f}".format(descuento))
        print("IVA: ${:.2f}".format(iva))
        print("Total: ${:.2f}".format(total))

        confirmacion = input("\n¿Desea proceder con el pago? (S/N): ")
        if confirmacion.lower() == "s":
            print("Pago exitoso.")
            print("Token de entrada: ", entrada.token)
            return True
        else:
            print("Pago cancelado.")
            return False

    def menu(self):
        print("Menú:")
        print("1. Comprar entrada")
        print("2. Salir")
        opcion = int(input("Seleccione una opción: "))
        return opcion

    def guardar_venta(self, entrada):
        with open("datos/ventas.txt", "a") as file:
            file.write(str(entrada) + "\n")

    def comprar_entrada(self):
        cliente = self.preguntar_datos_cliente()
        entrada = self.vender_entrada(cliente)
        subtotal, descuento, iva, total = self.calcular_costo_entrada(entrada)
        if self.confirmar_pago(entrada, subtotal, descuento, iva, total):
            self.guardar_cliente_token(cliente, entrada.token)
            self.guardar_venta(entrada)
    def actualizar_asientos_txt(self, carrera):
        with open(f"datos/asientos_carrera_{carrera.numero}.txt", "w") as file:
            for fila in range(len(carrera.asientos)):
                for columna in range(len(carrera.asientos[fila])):
                    estado = "D" if carrera.asientos[fila][columna] else "L"  # D = Disponible, L = No disponible
                    file.write(f"{estado}({fila + 1},{columna + 1}) ")
                file.write("\n")
                
                
                
    
    def start(self):
        volver_al_menu_principal = False
        while True:
            opcion = self.menu()
            if opcion == 1:
                self.comprar_entrada()
            elif opcion == 2:
                print("Gracias por usar nuestro sistema.")
                break
            else:
                print("Opción no válida, por favor intente nuevamente.")
                volver_al_menu_principal = True
        return volver_al_menu_principal  # Asegurarse de que el 'return' esté fuera del bucle 'while'


        
        

