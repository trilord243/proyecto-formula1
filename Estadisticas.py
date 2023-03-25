#Se importa la libreria request
import requests
#Importar las librerias de matlib.pyplot
import matplotlib.pyplot as plt

#Clase de estadisticas
class Estadisticas:
    def __init__(self):
        #Costo de la entrada vip
        self.costo_entrada_vip = 340
        #Url del api de carreras
        self.url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        #Lista de carreras
        self.carreras_data = []

    def cargar_datos(self):
        # Cargar datos de la API
        response = requests.get(self.url)
        self.carreras_data = response.json()
        
    #Metodo que busca la carrera con mayor boletos vendidos
    def carrera_mayor_boletos_vendidos(self):
        #Se crea un diccionario vacio para luego insertar los datos 
        boletos_vendidos = {}
        #Se itera el api de carreras
        for carrera in self.carreras_data:
            #Se guarda en una variable el nombre de las carreras
            nombre_carrera = carrera["name"]
            #Se guarda en el diccionario el nombre de carreras y asignarle un numero 0
            boletos_vendidos[nombre_carrera] = 0
        #Se abre el txt de tokes que tiene la informacion de los boletos vendidos 
        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(',')
                #Se guarda una variable con el no,nre de la carrera
                nombre_carrera = campos[3]
            
                #Se modifica el diccionario de boletos vendidos. Si se consigue la carrera entonces se le suma uno al valor del diccionario y con el metodo get si no lo encuentra el valor por defecto es 0
                boletos_vendidos[nombre_carrera] = boletos_vendidos.get(nombre_carrera, 0) + 1
        #Se guarda en una variable la carrera con el mayor boletos vendidos en el diccionario 
        carrera_mayor_boletos_vendidos = max(boletos_vendidos, key=boletos_vendidos.get)
        #Se regresa el valor del boleto mas vendido 
        return carrera_mayor_boletos_vendidos
    
    #Metodo que busca la carrera con mayor relacion de boletos vendidos y asistencia :D
    def estadisticas_asistencia(self):
        #Se crea un diccionario vacio 
        asistencia = {}
        #Se itera la lista que contiene las carreras
        for carrera in self.carreras_data:
            #Se guarda en una variable el nombre del circuito
            circuit_name = carrera["circuit"]["name"]
            #Se guarda en una variable el nombre de la carrera
            nombre_carrera = carrera["name"]
            #Se le agrega datos al diccionario asistenca que tendra dentro de el otro diccionario que estara el nombre del circuito , la cantidad de boletos vendidos y la cantidad de personas que asistieron 
            asistencia[nombre_carrera] = {"circuit": circuit_name, "boletos_vendidos": 0, "personas_asistieron": 0}
            
        #Se abre el archivo tokens.txt que tiene todos los datos de la asistencia de las carreras y de los boletos vendidos 
        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(',')
                #Se le asigna el nombre de la carrera a la variable nombre_carrera
                nombre_carrera = campos[3]
                #Se modifica el diccionario si coincide el nombre de la carrera y se le suma 1 al boleto vendido 
                asistencia[nombre_carrera]["boletos_vendidos"] += 1
                #Si la persona va  a asistir se le suma un al dato si las personas van a personas_asistieron
                if campos[6] == "Asistirá":
                    asistencia[nombre_carrera]["personas_asistieron"] += 1
        #Se itera el diccionario inicial con todos los datos actualizados 
        for nombre_carrera, stats in asistencia.items():
            #Si hay boletos vendidos entonces se saca la relacion entre las personas que asistieron con los boletos vendidos 
            if stats["boletos_vendidos"] > 0:
                stats["relacion_asistencia_venta"] = stats["personas_asistieron"] / stats["boletos_vendidos"]
            #Si no hay boletos vendudos entonces la relacion es 0 recordando que una division por 0 es indefinida 
            else:
                stats["relacion_asistencia_venta"] = 0
        #Se ordena la asistencia mediante el sort
        asistencia_ordenada = sorted([(nombre_carrera, stats) for nombre_carrera, stats in asistencia.items() if stats["boletos_vendidos"] > 0], key=lambda x: x[1]["relacion_asistencia_venta"], reverse=True)

        #Se imprime en forma de tabla los valores ordenados de mayor a menor Se utiliza el metodo.format para indicarle el formato en el que se quiere ser entregado 
        print("Carrera | Circuito | Boletos vendidos | Personas asistieron | Relación asistencia/venta")
        for nombre_carrera, stats in asistencia_ordenada:
            print("{} | {} | {} | {} | {:.2f}".format(
                nombre_carrera,
                stats["circuit"],
                stats["boletos_vendidos"],
                stats["personas_asistieron"],
                stats["relacion_asistencia_venta"]
            ))
            #Se devuelve la asistencia ordenada
        return asistencia_ordenada
    
    

 
    #Metodo que busca lor 3 productos mas vendidos en el restaurante 
    def top_productos_vendidos(self):
        #Se crea una lista vacia en donde se gardaren los daots 
        productos_vendidos = {}
        #Se busca en el txt de ventas realizadas donde estan los datos 
        with open("datos/ventas_realizadas.txt", "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(',')
                #Se le asigna a la variable producto el valor del nombre del producto 
                producto = campos[1]
                #Si el producto no se encuentra en productos vendidos entonces sele sumara 0
                if producto not in productos_vendidos:
                    productos_vendidos[producto] = 0
                #Si el producto_vendido existe entonces se le sumara 1
                productos_vendidos[producto] += 1
        #Se ordena de forma ordenada los productos mas vendidos aparecenran de primero en la lista ya que sera de forma desendente
        top_productos = sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)
        #Devuelve una sublista en donde se envientra los 3 productos mas vendidos :D
        return top_productos[:3]
    
    #Metodo que devielve las carreras ordenadas por asistencia es parecido al metodo de mostrar tabla de asistencia 
    def carreras_ordenadas_por_asistencia(self):
        #diccionario vacio que contendra las carreras ordenadas por asistencia
        asistencia = {}
        #Se itera el api de carreras
        for carrera in self.carreras_data:
            #Se guarda el nombre de la carrera en una variable 
            nombre_carrera = carrera["name"]
            #Se guarda en el diccionario el nombre de la carrera y asignarle un numero 0
            asistencia[nombre_carrera] = 0
        #Se abre el txt de tokes que tiene la informacion de las carreras ordenadas 
        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(',')
                #
                nombre_carrera = campos[3]
                if campos[6] == "Asistirá":
                    asistencia[nombre_carrera] += 1

        asistencia_ordenada = dict(sorted(asistencia.items(), key=lambda x: x[1], reverse=True))
        return asistencia_ordenada

    #Metodo que devuelve la carrera con mayor asistencia 
    def carrera_mayor_asistencia(self):
        asistencia_ordenada = self.carreras_ordenadas_por_asistencia()
        #Se obtiene el primer elemento de la lista ordenada con next(iter(asistencia_ordenada))
        carrera_con_mayor_asistencia = next(iter(asistencia_ordenada))
        return carrera_con_mayor_asistencia


    #Metodo que devuelve los boletos de manera ordenada 
    def carreras_ordenadas_por_boletos_vendidos(self):
        boletos_vendidos = {}
        for carrera in self.carreras_data:
            #Se hace el procedimiento de los metodos anteriores para obtener los boletos vendidos de mayor a menor 
            nombre_carrera = carrera["name"]
            boletos_vendidos[nombre_carrera] = 0
        
        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(',')
                nombre_carrera = campos[3]
                boletos_vendidos[nombre_carrera] += 1

        boletos_vendidos_ordenados = dict(sorted(boletos_vendidos.items(), key=lambda x: x[1], reverse=True))
        return boletos_vendidos_ordenados
    #Igual que ele metodo anterior se devuelve el boleto mas vendido 
    def carrera_mayor_boletos_vendidos(self):
        boletos_vendidos_ordenados = self.carreras_ordenadas_por_boletos_vendidos()
        carrera_con_mayor_boletos_vendidos = next(iter(boletos_vendidos_ordenados))
        return carrera_con_mayor_boletos_vendidos


    #Metodo que ordena todos los productos de manera ascendente
    def productos_ordenados_por_ventas(self):
        ventas_productos = {}

        with open("datos/ventas_realizadas.txt", "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(',')
                #Se guarda el nombre del producto 
                producto = campos[1]
                #La cantidad en flotante ya que son datos flotantes 
                cantidad = float(campos[3])
                #Si el producto se encuentra se le suma la cantidad 
                if producto in ventas_productos:
                    ventas_productos[producto] += cantidad
                #Si no se encuentra mas se le deja la cantidad inicial esto es para que se sumen cada uno de los productos 
                else:
                    ventas_productos[producto] = cantidad
        #Como se hizo anteriormente se ordenan los productos de manera ascendente
        ventas_productos_ordenados = dict(sorted(ventas_productos.items(), key=lambda x: x[1], reverse=True))
        return ventas_productos_ordenados
    
    
    #Metodo para obtener la carrera donde va a una cedula 
    def obtener_carrera_por_cedula(self, cedula):
        with open("datos/ventas_realizadas.txt", "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(",")
                #Se guarda la cedula del cliente u la carrera en una variable y si coinciden entonces devuelve la carrera de la cedula ingresada por parametro si no la encuentra devuelve None 
                cedula_ventas = campos[0]
                carrera = campos[2]
                if cedula_ventas == cedula:
                    return carrera
        return None
    
    
    
    
    #Metodo que calcula el prodedio de gasto de los vips por cada carrera 
    def calcular_promedio_gasto_vip_por_carrera(self):
        #Se crean los respectivos diccionarios para guardar los datos
        #Diccionario de gastor por carrera
        gastos_por_carrera = {}
        #Diccionario de gastos totales por cedula
        gastos_totales_por_cedula = {}
        #La cantidad de vip por cedula
        entradas_vip_por_cedula = {}
        # Se abre el txt donde se encuentran dichos datos 
        with open("datos/ventas_realizadas.txt", "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(",")
                #La cedula del cleinte se encuentra en el campo 1
                cedula = campos[0]
                #La carrera se encuentra en el campo 3
                carrera = campos[2]
                #Y el total gastado se enceuntra en el campo 4 y es un dato flotante
                total_gasto = float(campos[4])
                #Si en la iteracion la cedula no se eencuentra en los gastos totales entonces se dejan los valores iniciales y se guarda el costo de la entrada que es un dato constante 
                if cedula not in gastos_totales_por_cedula:
                    gastos_totales_por_cedula[cedula] = total_gasto
                    entradas_vip_por_cedula[cedula] = self.costo_entrada_vip
                else:
                    #Si se encuentra se le suman el gasto al cleinte 
                    gastos_totales_por_cedula[cedula] += total_gasto
        #Se itera el diccionario de gastos totales por cedula para actualizar sus datos 
        for cedula, total_gasto in gastos_totales_por_cedula.items():
            #Se le suman al gasto total las entradas vip por cedula y con el metodo obtener_carrera_por_cedula se optiene la carrera donde va  esa cedula
            total_gasto += entradas_vip_por_cedula[cedula]
            carrera = self.obtener_carrera_por_cedula(cedula)
            # Se agrega a la carrera los gastos 
            if carrera not in gastos_por_carrera:
                gastos_por_carrera[carrera] = [total_gasto]
            else:
                gastos_por_carrera[carrera].append(total_gasto)
        #Se crea un diccionario vacio para sacar el promedio
        promedio_gasto_por_carrera = {}
        for carrera, gastos in gastos_por_carrera.items():
            #Se saca el promedio total de los clientes por cada carrera  que la sumatoria de los gastos sobre el numero de gastos que se realizaron 
            promedio_gasto_por_carrera[carrera] = sum(gastos) / len(gastos)

        return promedio_gasto_por_carrera


    
    #Metodo para obtener los primeros 3 clientes que mas gastaron 
    def top_3_clientes(self):
        #Un diccionario vacio para guardar los clientes 
        clientes = {}
        #Se abre el txt donde se encuentran dichos datos 
        with open("datos/tokens.txt", 'r') as file:
            for line in file.readlines():
                tokens = line.strip().split(',')
                #Se guarda los datos de la cedula 
                cedula = tokens[2]
                #Por cada cedula se le va asignar el valor de uno si se encuentran mas cedulas en el txt se le va sumando 1 
                if cedula in clientes:
                    clientes[cedula] += 1
                else:
                    clientes[cedula] = 1
        #De forma ordenada desendente se ordena la lsota de los clientes y se retorna los primeros 3 clientes graccas a [:3] Ya que solo queremos los 3 cleitnes 
        top_clientes = sorted(clientes.items(), key=lambda x: x[1], reverse=True)[:3]
        return top_clientes
    
    #Grafico de promedio de vip por carrera 
    def grafico_promedio_gasto_vip_por_carrera(self):
        #Se guarda en una variable el metodo de donde se calcula el promedio de vip por carrera 
        promedio_gasto_por_carrera = self.calcular_promedio_gasto_vip_por_carrera()
        #Se transgorma en una lista los nombres de las carreras 
        carreras = list(promedio_gasto_por_carrera.keys())
        #Se transgorma en una lista los promedios de las carreras 
        promedios = list(promedio_gasto_por_carrera.values())
        #plt recibe 2 parametros para la grafica (x) que seran las carreras y los promedios en (y)
        plt.bar(carreras, promedios)
        #El eje x se le agrega el nombre de carreas 
        plt.xlabel('Carreras')
        #Se le llama al eje y el nombre 
        plt.ylabel('Gasto promedio en $')
        #El Se le agrega el titulo de la grafica 
        plt.title('Promedio de gasto VIP por carrera')
        #Se le pone el tamaño deseado de la grafica para que sea visible 
        plt.subplots_adjust(bottom=0.37) 
        #Los nombres en x se rotan 45 grados 
        plt.xticks(rotation=45)
        #plt.show hace que la grafica se muestre 
        plt.show()
    
    #Grafico que muestra la relacion de ventas por carrerra 
    def grafico_relacion_asistencia_venta_por_carrera(self, asistencia_ordenada):
        #En una lista carrera se agregan unicamente el nombre de las carreras que estan en el iterable que esa por parametros 
        carreras = [nombre_carrera for nombre_carrera, stats in asistencia_ordenada]
        #Una En una lista de relaciones de asistencia de ventas que va a obterner los de las relaciones de asistencias 
        relaciones_asistencia_venta = [stats["relacion_asistencia_venta"] for nombre_carrera, stats in asistencia_ordenada]
        #Se hace la grafica con los metodos que da matlib 
        plt.figure(figsize=(12, 6))
        plt.bar(carreras, relaciones_asistencia_venta)
        plt.xlabel('Carreras')
        plt.ylabel('Relación asistencia/venta')
        plt.title('Relación asistencia/venta por carrera')
        plt.subplots_adjust(bottom=0.37)
        plt.xticks(rotation=45)
        plt.show()

    #Graficio de carreas con mayor asistencias 
    def grafico_carreras_mayor_asistencia(self):
        #Se guarda en una variable los metodos de la asistencia ordena 
        asistencia_ordenada = self.carreras_ordenadas_por_asistencia()
        #Se guarda en una lista los keys de el diccionario que estan las carreras
        carreras = list(asistencia_ordenada.keys())
        #Se guarda en una lista los valores de el diccionario que estan las asistencias por cada carrera
        asistencias = list(asistencia_ordenada.values())
        #Se hace la grafica con los metodos que da matlib
        plt.figure(figsize=(12, 6))
        plt.bar(carreras, asistencias)
        plt.xlabel('Carreras')
        plt.ylabel('Asistencia')
        plt.title('Asistencia por carrera (de mayor a menor)')
        plt.subplots_adjust(bottom=0.37)
        plt.xticks(rotation=90)
        plt.show()

    #Grafico de carrreras con mayor boleto vendido 
    def grafico_carreras_mayor_boletos_vendidos(self):
        #Se guarda en una variable las carreras ordenadas por boletos vendidos 
        boletos_vendidos_ordenados = self.carreras_ordenadas_por_boletos_vendidos()
        #Se guardan las carreras ordenadas por boletos vendidos 
        carreras = list(boletos_vendidos_ordenados.keys())
        #Se guardan en una lista la cantidad de boletos vendidos por cada carrera 
        cantidad_boletos = list(boletos_vendidos_ordenados.values())
        #Se hace la grafica con los metodos que da matlib 
        plt.figure(figsize=(12, 6))
        plt.bar(carreras, cantidad_boletos)
        plt.xlabel('Carreras')
        plt.ylabel('Cantidad de boletos vendidos')
        plt.title('Carreras con mayor cantidad de boletos vendidos')
        plt.subplots_adjust(bottom=0.37)
        plt.xticks(rotation=45)
        plt.show() 


    #Grafico de los productos que tuvieron mas ventas 
    def grafico_productos_mayor_ventas(self):
        #Se guarda en una variable los productos ordenados por ventas 
        ventas_productos_ordenados = self.productos_ordenados_por_ventas()
        #Se guarda en una lista los productos 
        productos = list(ventas_productos_ordenados.keys())
        #Se guarda en una lista la cantidad vendida por cada producto 
        cantidad_vendida = list(ventas_productos_ordenados.values())
        #Se hace la grafica con los metodos que da matlib 
        plt.figure(figsize=(12, 6))
        plt.bar(productos, cantidad_vendida)
        plt.xlabel('Productos')
        plt.ylabel('Cantidad vendida')
        plt.title('Productos con mayor cantidad vendida en el restaurante')
        plt.subplots_adjust(bottom=0.25)
        plt.xticks(rotation=45)
        plt.show()
    
    #Grafica de los top 3 clientes 
    def grafico_top_3_clientes(self):
        #Se llama al metodo doonde estan los 3 cleitnes 
        top_clientes = self.top_3_clientes()
        nombres = []
        frecuencias = []
        #Se guarda en una lista los nombre de los clientes y la frecuencia que tienen
        for cliente, frecuencia in top_clientes:
            nombres.append(cliente)
            frecuencias.append(frecuencia)
        # Se hace la grafica con los metodos que da matlib 
        
        plt.bar(nombres, frecuencias)
        plt.xlabel("Clientes")
        plt.ylabel("Frecuencia")
        plt.title("Top 3 clientes")
        plt.show()

    
    #El metodo start para inicializar el modulo 
    def start(self):
        #Se cargan los datos de la apo 
        self.cargar_datos()
        #Se muestra el menu 
        menu_estat=True
        while menu_estat:
            print("\nMenú de estadísticas:")
            print("1. Promedio de gasto VIP por carrera")
            print("2. Estadísticas de asistencia")
            print("3. Carrera con mayor asistencia")
            print("4. Carrera con mayor cantidad de boletos vendidos")
            print("5. Top 3 productos más vendidos en el restaurante")
            print("6. Top 3 clientes que más compraron boletos")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                promedio_gasto_por_carrera = self.calcular_promedio_gasto_vip_por_carrera()
                print("\nPromedio de gasto VIP por carrera:\n")
                #Se itera los datos para mostrarlos por consola de forma ordenada 
                for carrera, promedio in promedio_gasto_por_carrera.items():
                    print(f"\n{carrera}: ${promedio:.2f}\n")
                    #Se llama al grafico que muestra el promedio de gasto VIP por carrera 
                self.grafico_promedio_gasto_vip_por_carrera()
            elif opcion == "2":
                #Se llama al metodo que muestra las estadísticas de asistencia
                asistencia_ordenada = self.estadisticas_asistencia()
                #Se llama al grafico que muestra las estadísticas de asistencia 
                self.grafico_relacion_asistencia_venta_por_carrera(asistencia_ordenada)
              
            elif opcion == "3":
                #Se llama al metodo  que muestra las carreras con mayor asistencia 
                carrera_con_mayor_asistencia = self.carrera_mayor_asistencia()
                print("\nLa carrera con mayor asistencia fue:", carrera_con_mayor_asistencia)
                self.grafico_carreras_mayor_asistencia()
                
               
                
                
            elif opcion == "4":
                carrera_con_mayor_boletos_vendidos = self.carrera_mayor_boletos_vendidos()
                print("\nLa carrera con mayor cantidad de boletos vendidos fue:", carrera_con_mayor_boletos_vendidos)
                self.grafico_carreras_mayor_boletos_vendidos()
            elif opcion == "5":
                top_3_productos = self.top_productos_vendidos()
                print("\nTop 3 productos más vendidos en el restaurante:\n")
                self.grafico_productos_mayor_ventas()
                for i, producto in enumerate(top_3_productos, 1):
                    print(f"\n{i}. {producto[0]}: {producto[1]} ventas\n")
            elif opcion == "6":
                top_clientes = self.top_3_clientes()
                for cedula, boletos_comprados in top_clientes:
                    print(f"\nLa cédula {cedula} compró {boletos_comprados} boletos.\n")
                self.grafico_top_3_clientes()
                
            elif opcion == "0":
                print("Saliendo del menú de estadísticas...")
                menu_estat=False
            else:
               menu_estat=False
