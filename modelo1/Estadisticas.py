
import requests
import matplotlib.pyplot as plt
class Estadisticas:
    def __init__(self, archivo_ventas="datos/ventas_realizadas.txt",archivo_tokens="datos/tokens.txt"):
        self.archivo_ventas = archivo_ventas
        self.archivo_tokens = archivo_tokens
        self.costo_entrada_vip = 340
        self.url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        self.races_data = []

    def cargar_datos(self):
        # Cargar datos de la API
        response = requests.get(self.url)
        self.races_data = response.json()
        
    
    def carrera_mayor_boletos_vendidos(self):
        boletos_vendidos = {}
        for race in self.races_data:
            race_name = race["name"]
            boletos_vendidos[race_name] = 0

        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(',')
                race_name = campos[3]
                boletos_vendidos[race_name] = boletos_vendidos.get(race_name, 0) + 1

        carrera_mayor_boletos_vendidos = max(boletos_vendidos, key=boletos_vendidos.get)
        return carrera_mayor_boletos_vendidos
    
    def estadisticas_asistencia(self):
        asistencia = {}
        for race in self.races_data:
            circuit_name = race["circuit"]["name"]
            race_name = race["name"]
            asistencia[race_name] = {"circuit": circuit_name, "boletos_vendidos": 0, "personas_asistieron": 0}
            

        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(',')
                race_name = campos[3]
                asistencia[race_name]["boletos_vendidos"] += 1
                if campos[6] == "Asistirá":
                    asistencia[race_name]["personas_asistieron"] += 1

        for race_name, stats in asistencia.items():
            if stats["boletos_vendidos"] > 0:
                stats["relacion_asistencia_venta"] = stats["personas_asistieron"] / stats["boletos_vendidos"]
            else:
                stats["relacion_asistencia_venta"] = 0

        asistencia_ordenada = sorted([(race_name, stats) for race_name, stats in asistencia.items() if stats["boletos_vendidos"] > 0], key=lambda x: x[1]["relacion_asistencia_venta"], reverse=True)


        print("Carrera | Circuito | Boletos vendidos | Personas asistieron | Relación asistencia/venta")
        for race_name, stats in asistencia_ordenada:
            print("{} | {} | {} | {} | {:.2f}".format(
                race_name,
                stats["circuit"],
                stats["boletos_vendidos"],
                stats["personas_asistieron"],
                stats["relacion_asistencia_venta"]
            ))
        return asistencia_ordenada
    def obtener_circuito_por_carrera(self, nombre_carrera):
        for race in self.races_data:
            if race["name"] == nombre_carrera:
                return race["circuit"]["name"]
        return None
 
 
    def top_productos_vendidos(self):
        productos_vendidos = {}

        with open("datos/ventas_realizadas.txt", "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(',')
                producto = campos[1]
                if producto not in productos_vendidos:
                    productos_vendidos[producto] = 0
                productos_vendidos[producto] += 1

        top_productos = sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)
        return top_productos[:3]
 
    def carreras_ordenadas_por_asistencia(self):
        asistencia = {}
        for race in self.races_data:
            race_name = race["name"]
            asistencia[race_name] = 0

        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(',')
                race_name = campos[3]
                if campos[6] == "Asistirá":
                    asistencia[race_name] += 1

        asistencia_ordenada = dict(sorted(asistencia.items(), key=lambda x: x[1], reverse=True))
        return asistencia_ordenada

    
    def carrera_mayor_asistencia(self):
        asistencia_ordenada = self.carreras_ordenadas_por_asistencia()
        carrera_con_mayor_asistencia = next(iter(asistencia_ordenada))
        return carrera_con_mayor_asistencia

    def carreras_ordenadas_por_boletos_vendidos(self):
        boletos_vendidos = {}
        for race in self.races_data:
            race_name = race["name"]
            boletos_vendidos[race_name] = 0

        with open("datos/tokens.txt", "r") as tokens_file:
            for linea in tokens_file:
                campos = linea.strip().split(',')
                race_name = campos[3]
                boletos_vendidos[race_name] += 1

        boletos_vendidos_ordenados = dict(sorted(boletos_vendidos.items(), key=lambda x: x[1], reverse=True))
        return boletos_vendidos_ordenados
    
    def carrera_mayor_boletos_vendidos(self):
        boletos_vendidos_ordenados = self.carreras_ordenadas_por_boletos_vendidos()
        carrera_con_mayor_boletos_vendidos = next(iter(boletos_vendidos_ordenados))
        return carrera_con_mayor_boletos_vendidos

    def clientes_ordenados_por_ventas(self):
        venta_clientes = {}
        with open("datos/ventas_realizadas,txt", "r") as ventas_file:
            for linea in ventas_file:
                campos=linea.strip().split(',')
       
    def productos_ordenados_por_ventas(self):
        ventas_productos = {}

        with open("datos/ventas_realizadas.txt", "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(',')
                producto = campos[1]
                cantidad = float(campos[3])

                if producto in ventas_productos:
                    ventas_productos[producto] += cantidad
                else:
                    ventas_productos[producto] = cantidad

        ventas_productos_ordenados = dict(sorted(ventas_productos.items(), key=lambda x: x[1], reverse=True))
        return ventas_productos_ordenados

    
    
    
    def calcular_promedio_gasto_vip_por_carrera(self):
        gastos_por_carrera = {}
        gastos_totales_por_cedula = {}
        entradas_vip_por_cedula = {}

        with open(self.archivo_ventas, "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(",")
                cedula = campos[0]
                carrera = campos[2]
                total_gasto = float(campos[4])

                if cedula not in gastos_totales_por_cedula:
                    gastos_totales_por_cedula[cedula] = total_gasto
                    entradas_vip_por_cedula[cedula] = self.costo_entrada_vip
                else:
                    gastos_totales_por_cedula[cedula] += total_gasto

        for cedula, total_gasto in gastos_totales_por_cedula.items():
            total_gasto += entradas_vip_por_cedula[cedula]
            carrera = self.obtener_carrera_por_cedula(cedula)
            if carrera not in gastos_por_carrera:
                gastos_por_carrera[carrera] = [total_gasto]
            else:
                gastos_por_carrera[carrera].append(total_gasto)

        promedio_gasto_por_carrera = {}
        for carrera, gastos in gastos_por_carrera.items():
            promedio_gasto_por_carrera[carrera] = sum(gastos) / len(gastos)

        return promedio_gasto_por_carrera

    def obtener_carrera_por_cedula(self, cedula):
        with open(self.archivo_ventas, "r") as ventas_file:
            for linea in ventas_file:
                campos = linea.strip().split(",")
                cedula_ventas = campos[0]
                carrera = campos[2]
                if cedula_ventas == cedula:
                    return carrera
        return None
    def top_3_clientes(self):
        clientes = {}

        with open("datos/tokens.txt", 'r') as file:
            for line in file.readlines():
                tokens = line.strip().split(',')
                cedula = tokens[2]

                if cedula in clientes:
                    clientes[cedula] += 1
                else:
                    clientes[cedula] = 1

        top_clientes = sorted(clientes.items(), key=lambda x: x[1], reverse=True)[:3]
        return top_clientes
    
    def grafico_promedio_gasto_vip_por_carrera(self,estadisticas):
        promedio_gasto_por_carrera = estadisticas.calcular_promedio_gasto_vip_por_carrera()
        carreras = list(promedio_gasto_por_carrera.keys())
        promedios = list(promedio_gasto_por_carrera.values())

        plt.bar(carreras, promedios)
        plt.xlabel('Carreras')
        plt.ylabel('Gasto promedio en $')
        plt.title('Promedio de gasto VIP por carrera')
        plt.subplots_adjust(bottom=0.37)
        plt.xticks(rotation=90)
        plt.show()
    
    def grafico_relacion_asistencia_venta_por_carrera(self, asistencia_ordenada):
        carreras = [race_name for race_name, stats in asistencia_ordenada]
        relaciones_asistencia_venta = [stats["relacion_asistencia_venta"] for race_name, stats in asistencia_ordenada]

        plt.figure(figsize=(12, 6))
        plt.bar(carreras, relaciones_asistencia_venta)
        plt.xlabel('Carreras')
        plt.ylabel('Relación asistencia/venta')
        plt.title('Relación asistencia/venta por carrera')
        plt.subplots_adjust(bottom=0.37)
        plt.xticks(rotation=90)
        plt.show()

    def grafico_carreras_mayor_asistencia(self):
        asistencia_ordenada = self.carreras_ordenadas_por_asistencia()
        carreras = list(asistencia_ordenada.keys())
        asistencias = list(asistencia_ordenada.values())

        plt.figure(figsize=(12, 6))
        plt.bar(carreras, asistencias)
        plt.xlabel('Carreras')
        plt.ylabel('Asistencia')
        plt.title('Asistencia por carrera (de mayor a menor)')
        plt.subplots_adjust(bottom=0.37)
        plt.xticks(rotation=90)
        plt.show()


    def grafico_carreras_mayor_boletos_vendidos(self):
        boletos_vendidos_ordenados = self.carreras_ordenadas_por_boletos_vendidos()
        carreras = list(boletos_vendidos_ordenados.keys())
        cantidad_boletos = list(boletos_vendidos_ordenados.values())

        plt.figure(figsize=(12, 6))
        plt.bar(carreras, cantidad_boletos)
        plt.xlabel('Carreras')
        plt.ylabel('Cantidad de boletos vendidos')
        plt.title('Carreras con mayor cantidad de boletos vendidos')
        plt.subplots_adjust(bottom=0.37)
        plt.xticks(rotation=90)
        plt.show() 


        
    def grafico_productos_mayor_ventas(self):
        ventas_productos_ordenados = self.productos_ordenados_por_ventas()
        productos = list(ventas_productos_ordenados.keys())
        cantidad_vendida = list(ventas_productos_ordenados.values())

        plt.figure(figsize=(12, 6))
        plt.bar(productos, cantidad_vendida)
        plt.xlabel('Productos')
        plt.ylabel('Cantidad vendida')
        plt.title('Productos con mayor cantidad vendida en el restaurante')
        plt.subplots_adjust(bottom=0.25)
        plt.xticks(rotation=45)
        plt.show()
    
    
    def grafico_top_3_clientes(self):
        top_clientes = self.top_3_clientes()
        nombres = []
        frecuencias = []
        for cliente, frecuencia in top_clientes:
            nombres.append(cliente)
            frecuencias.append(frecuencia)

        plt.bar(nombres, frecuencias)
        plt.xlabel("Clientes")
        plt.ylabel("Frecuencia")
        plt.title("Top 3 clientes")
        plt.show()

    
    
    def start(self):
        estadisticas = Estadisticas()
        estadisticas.cargar_datos()
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
                promedio_gasto_por_carrera = estadisticas.calcular_promedio_gasto_vip_por_carrera()
                print("\nPromedio de gasto VIP por carrera:\n")
                self.grafico_promedio_gasto_vip_por_carrera(estadisticas)
                for carrera, promedio in promedio_gasto_por_carrera.items():
                    print(f"\n{carrera}: ${promedio:.2f}\n")
            elif opcion == "2":
                asistencia_ordenada = estadisticas.estadisticas_asistencia()
                estadisticas.grafico_relacion_asistencia_venta_por_carrera(asistencia_ordenada)
              
            elif opcion == "3":
                carrera_con_mayor_asistencia = estadisticas.carrera_mayor_asistencia()
                print("\nLa carrera con mayor asistencia fue:", carrera_con_mayor_asistencia)
                estadisticas.grafico_carreras_mayor_asistencia()
                
               
                
                
            elif opcion == "4":
                carrera_con_mayor_boletos_vendidos = estadisticas.carrera_mayor_boletos_vendidos()
                print("\nLa carrera con mayor cantidad de boletos vendidos fue:", carrera_con_mayor_boletos_vendidos)
                estadisticas.grafico_carreras_mayor_boletos_vendidos()
            elif opcion == "5":
                top_3_productos = estadisticas.top_productos_vendidos()
                print("\nTop 3 productos más vendidos en el restaurante:\n")
                estadisticas.grafico_productos_mayor_ventas()
                for i, producto in enumerate(top_3_productos, 1):
                    print(f"\n{i}. {producto[0]}: {producto[1]} ventas\n")
            elif opcion == "6":
                top_clientes = estadisticas.top_3_clientes()
                for cedula, boletos_comprados in top_clientes:
                    print(f"\nLa cédula {cedula} compró {boletos_comprados} boletos.\n")
                estadisticas.grafico_top_3_clientes()
                
            elif opcion == "0":
                print("Saliendo del menú de estadísticas...")
                menu_estat=False
            else:
               menu_estat=False
