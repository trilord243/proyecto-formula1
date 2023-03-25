import requests
#Importa la libreria de json que al llamar al api con su metodo json.loads transforma el json en un diccionario
import json
#Se importa la libreria de uuid para poder hacer tokens unicos 
import uuid
#Se importa la clase Cliente
from clases.Cliente import Cliente

#Se crea la clase venta de entradas
class Venta_entradas:
    def __init__(self):
        #El api que se va a utilizar 
        self.url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        #Se guardan los datos de la carrera
        self.carreras = self.cargar_carreras()

    #Metodo llama el api para cargar las carreras
    def cargar_carreras(self):
        response = requests.get(self.url)
        carreras = json.loads(response.text)
        return carreras
                    

    #Metodo para cargar los asientos disponibles y crear los asientos que se ocuparan para las carreras 
    def cargar_asientos_disponibles(self, carrera):
        
        try:
            #Se abre el archivo con los asientos por la carrera que recibe como parametro 
            with open(f"datos/asientos_{carrera}.txt", "r") as archivo_asientos:
                asientos_ocupados = archivo_asientos.read().splitlines()
                # Se crea unalista que almacena los asientos ocupados en un archivo para una carrera específica. Cada línea del archivo representa un asiento ocupado y se almacena como un par de números enteros separados por comas (Fila,columna)
                asientos_ocupados = [tuple(map(int, asiento.split(','))) for asiento in asientos_ocupados]
                return asientos_ocupados
        except FileNotFoundError:
            return []
        
    
    
    #Metodo que muestra los asientos disponibles para una carrera específica
    def asiento_disponible(self, carrera, fila, asiento):
        asientos_ocupados = self.cargar_asientos_disponibles(carrera)
        return (fila, asiento) not in asientos_ocupados
    
    #Metodo que valida el rando que hay en las filas y las columnas de una carrera
    def asiento_en_rango(self, carrera, fila, asiento, tipo_entrada):
        filas, columnas = self.carreras[carrera]['map'][tipo_entrada]
        return 0 <= fila < filas and 0 <= asiento < columnas
   
    
    
        
    #Metodo que registra el asiento por carrera, la fila y el asiento 
    def registrar_asiento(self, carrera, fila, asiento):
        with open(f"datos/asientos_{carrera}.txt", "a") as archivo_asientos:
            archivo_asientos.write(f"{fila},{asiento}\n")
    #Metodo que muestra las carreras ordenadas 
    def mostrar_carreras(self):
        for i, carrera in enumerate(self.carreras):
            print(f"{i + 1}. {carrera['name']} - {carrera['date']} - {carrera['circuit']['name']}")
    
    
    #Metodo para ver si los asientos estan ocupados, para que el usuario no ingrese un asiento que esta ocupado 
    def todos_asientos_ocupados(self, carrera, tipo_entrada):
        filas, columnas = self.carreras[carrera]['map'][tipo_entrada]
        asientos_totales = filas * columnas
        asientos_ocupados = len(self.cargar_asientos_disponibles(self.carreras[carrera]['name']))
        
        return asientos_ocupados >= asientos_totales

    #Metodo para mostrar toods los asientos que estan disponibles 
    def mostrar_asientos_disponibles(self, carrera, tipo_entrada):
        if self.todos_asientos_ocupados(carrera, tipo_entrada):
            return 
        #Se hace una lista de las filas y columnas de la carrera
        filas, columnas = self.carreras[carrera]['map'][tipo_entrada]
        #Se guarda una variable que llama el metodo para saber que asientos que estan ocupados 
        asientos_ocupados = self.cargar_asientos_disponibles(self.carreras[carrera]['name'])
        #Se imprime las carreras que estan dispobimbes 
        print(f"Asientos disponibles para la entrada {tipo_entrada}:")
        #Se itera la lista de las filas y columnas de la carrera
        for i in range(filas):
            for j in range(columnas):
                #Si el asiento y la fila no estan ocupados imprime la matriz de la fila para que el usuario pueda escoger los asientos disponibles 
                if (i, j) not in asientos_ocupados:
                    #Se imprime las matrizes y con end=" " para que haya un espacio entre las matrices
                    print(f"[{i + 1},{j + 1}]", end=" ")
                else:
                    #Si no existre entonces muestra una x para no mostrar los asientos ocupados 
                    print("[X]", end=" ")
            print()

    #Metodo para obetener los datos del cliente,guarda y retorna ol objeto cliente 
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

    #Funcion para saber si un numero es ondulado 
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

    #Metoo para sacar el costo de la entrada para saber si darle un descuento al cliente o no en el precio final 
    def calcular_costo_entrada(self, tipo_entrada, cedula):
        #El precio base de una enreada feneral es 150 si es general o 340 si es vip
        precio_base = 150 if tipo_entrada == "general" else 340
        #Se calcula el descuento si el numero es ondulado y si no es ondulado regresa 1
        descuento = 0.5 if self.es_numero_ondulado(int(cedula)) else 1
        #EL subtotal 
        subtotal = precio_base * descuento
        #Se le agrega el iva
        iva = subtotal * 0.16
        #El precio total 
        total = subtotal + iva
        return subtotal, descuento, iva, total

    #Se guarda las ventas en un archivo.txt
    def guardar_venta(self, venta_info):
        try:
            with open("datos/ventas.txt", "a") as archivo_ventas:
                archivo_ventas.write(venta_info + "\n")
        except Exception as e:
            print("Error al guardar la venta:", e)

    #Se guarda el token con la informacion del cliente y la confirmacion de asistencia del cliente 
    def guardar_token(self, token_info):
        try:
            with open("datos/tokens.txt", "a") as archivo_tokens:
                archivo_tokens.write(token_info + ",Asistirá\n")  
        except Exception as e:
            print("Error al guardar el token:", e)

    
    
    #Funcion que genera token gracias a la liberira de uuid en forma de str
    def generar_token(self):
        return str(uuid.uuid4())
    
    
    #Menu principal de la aplicacion
    def start(self):
        #Carga los datos de los clientes 
        cliente = self.obtener_datos_cliente()
        #Funcion que muestra las carreras 
        self.mostrar_carreras()
        
        
       

       
        numero_carreras = len(self.carreras)
        carrera_menu=True
        while carrera_menu:
            #Se seleciona la carrera que se desea realizar la venta y se valida si esta en el rango del numeto de las carreras o si es un valor numerico 
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
            #Se pregunta el usuario si la entrada que quiere es vip o general
            tipo_entrada = input("Ingrese el tipo de entrada que desea comprar (general/vip): ").lower()
            if tipo_entrada == "vip" or tipo_entrada == "general":
                tipo_menu=False
            else:
                print("Por favor, ingrese 'general' o 'vip'.")
        #Metodo que muestra los avientos esta disponible 
        self.mostrar_asientos_disponibles(carrera_seleccionada, tipo_entrada)
        cerrar_menu = self.todos_asientos_ocupados(carrera_seleccionada, tipo_entrada)
        
        #Si no hay asientos disponibles muesta mensajes de que no hay asintos  
        if cerrar_menu:
            print("No hay asientos disponibles, saliendo del menú.")
        else:
            
            asiento_disponible = False
            
        
            while not asiento_disponible:
                menu_fila=True
                while menu_fila:
                    try:
                        #se escoge la fila que se desea comprar y se valida si es un valor numerico
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
                #Si el asiento esta en rango y sta disponible se sale del bucle si no esxite entonces  se sale del bucle
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
            
           
            #Se le muestra al cliente todos los datos de su compra 
            subtotal, descuento, iva, total = self.calcular_costo_entrada(tipo_entrada, cliente.cedula)
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Descuento: ${subtotal * (1 - descuento):.2f}")
            print(f"IVA: ${iva:.2f}")
            print(f"Total: ${total:.2f}")
            #Si el cliente quiere proceder se le genera un token 
            confirmar_compra = input("¿Desea proceder a pagar la entrada? (S/N): ").lower()
            if confirmar_compra == 's':
                token = self.generar_token()
                #Se guarda los datos del cliente y sus compras 
                venta_info = f"{cliente.nombre},{cliente.cedula},{cliente.edad},{self.carreras[carrera_seleccionada]['name']},{tipo_entrada},{total}"
                self.guardar_venta(venta_info)
                #Se guarda los datos del cliente, sus compras yu el token por cada entrada 
                token_info = f"{token},{cliente.nombre},{cliente.cedula},{self.carreras[carrera_seleccionada]['name']},{tipo_entrada},{total}"
                self.guardar_token(token_info)

                print("Pago exitoso.")
                #Se muestra el token 
                print(f"Su token de entrada es: {token}")  # Muestra el token al cliente
            else:
                print("Compra cancelada.")