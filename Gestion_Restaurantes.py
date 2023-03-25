#Importa el modulo de json que al llamar al api con su metodo json.loads transforma el json en un diccionario
import json
import requests
#Llamamos a la clase producto 
from clases.Producto import Producto
#Clase de Gestion de Restaurantes 
class Gestion_Restaurante:
    def __init__(self):
        #Se guarda el api que haremos 
        self.url = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        #Se guarda la dara de carreras 
        self.data = self.cargar_carrera()
        #Se guarda la dara de productos 
        self.productos = self.obtener_datos()

    #Metodo que permite cargar la dara de carreras 
    def cargar_carrera(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        return data
    
    
    #Metodo para obtener los datos de los productos  
    def obtener_datos(self):
        #Lista de productos vacia 
        productos = []
        #Se itera los datos de las carreras 
        for carrera in self.data:
            #Por cada restaurante que hay en cada carrera 
            for restaurant in carrera['restaurants']:
                #Y por cada items que hay en cada restaurante 
                for item in restaurant['items']:
                    #Se guarda el precio que se le multiplica el IVA
                    price = round(float(item['price']) * 1.16, 2)
                    #Se guardan los datos de los productos en las clase Producto
                    product = Producto(item['name'], item['type'], price)
                    #Se guarda cada clase en la lista de productos
                    productos.append(product)
        return productos
    
    #Metodo que busca filtra los productos por nombre,tipo,maximo y minimo
    def buscar(self, name=None, tipo_product=None, minimo=None, maximo=None):
        #Se guarda los productos 
        resultado = self.productos
        #Si alguno de los resultados no es None que es su valor por defecto entonces busca el resultdado 
        if name or tipo_product or minimo is not None or maximo is not None:
            if name:
                #Filtra los productos por nombre
                resultado = [p for p in resultado if name.lower() in p.name.lower()]
            if tipo_product:
                #Filtra los productos por tipo
                resultado = [p for p in resultado if tipo_product.lower() in p.product_type.lower()] # Modificado aquí
            if minimo is not None:
                #Por minimo y su maximo 
                resultado = [p for p in resultado if p.price >= minimo]
            if maximo is not None:
                resultado = [p for p in resultado if p.price <= maximo]
        else:
            print("Por favor, ingrese al menos un criterio de búsqueda.")
            return []

        return resultado

    #Metodo qu muestra el menu de la aplicacion 
    def start(self):
        print('Bienvenido al sistema de gestión de restaurantes de carreras F1 VIP')
        menu_val=True
        while menu_val:
            print('1. Buscar productos')
            print('2. Salir')
            option = input('Seleccione una opción: ')
            if option == '1':
                name = input('Ingrese el nombre del producto (opcional): ')
                tipo_product = input('Ingrese el tipo de producto (opcional): ')
                minimo = input('Ingrese el precio mínimo (opcional): ')
                maximo = input('Ingrese el precio máximo (opcional): ')

                
                name = name if name else None
                tipo_product = tipo_product if tipo_product else None

                # valida  en que el usuario ingrese un valor no numérico
                try:
                    minimo = float(minimo) if minimo else None
                except ValueError:
                    print("Error: Por favor, ingrese un valor numérico válido para el precio mínimo.")
                    continue

                try:
                    maximo = float(maximo) if maximo else None
                except ValueError:
                    print("Error: Por favor, ingrese un valor numérico válido para el precio máximo.")
                    continue

                resultado = self.buscar(name, tipo_product, minimo, maximo)

                if not resultado:
                    print('No se encontraron productos que coincidan con los criterios de búsqueda.')
                else:
                    #Se muestra todos los resultados 
                    print('Resultados de la búsqueda:')
                    for product in resultado:
                        print(product)

            elif option == '2':
                print('Gracias por usar el sistema de gestión de restaurantes de carreras F1 VIP')
                menu_val=False
            else:
                print('Opción inválida, por favor intente de nuevo.')