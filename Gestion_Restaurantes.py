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
    
    #Me
    def buscar(self, name=None, product_type=None, min_price=None, max_price=None):
        resultado = self.productos

        if name or product_type or min_price is not None or max_price is not None:
            if name:
                resultado = [p for p in resultado if name.lower() in p.name.lower()]
            if product_type:
                resultado = [p for p in resultado if product_type.lower() in p.product_type.lower()]
            if min_price is not None:
                resultado = [p for p in resultado if p.price >= min_price]
            if max_price is not None:
                resultado = [p for p in resultado if p.price <= max_price]
        else:
            print("Por favor, ingrese al menos un criterio de búsqueda.")
            return []

        return resultado


    def start(self):
        print('Bienvenido al sistema de gestión de restaurantes de carreras F1 VIP')
        menu_val=True
        while menu_val:
            print('1. Buscar productos')
            print('2. Salir')
            option = input('Seleccione una opción: ')
            if option == '1':
                name = input('Ingrese el nombre del producto (opcional): ')
                product_type = input('Ingrese el tipo de producto (opcional): ')
                min_price = input('Ingrese el precio mínimo (opcional): ')
                max_price = input('Ingrese el precio máximo (opcional): ')

                try:
                    if min_price:
                        min_price = float(min_price)
                    if max_price:
                        max_price = float(max_price)
                except ValueError:
                    print("Error: Por favor, ingrese un valor numérico válido para el precio mínimo y/o máximo.")
                    continue
                
                resultado = self.buscar(name, product_type, min_price, max_price)

                if not resultado:
                    print('No se encontraron productos que coincidan con los criterios de búsqueda.')
                else:
                    print('Resultados de la búsqueda:')
                    for product in resultado:
                        print(product)
                        
            elif option == '2':
                print('Gracias por usar el sistema de gestión de restaurantes de carreras F1 VIP')
                menu_val=False
            else:
                print('Opción inválida, por favor intente de nuevo.')
