import json
import requests
from clases.Producto import Producto

class Gestion_Restaurante:
    def __init__(self):
        self.url = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        self.data = self.cargar_carrera()
        self.productos = self.obtener_datos()

    def cargar_carrera(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        return data

    def obtener_datos(self):
        productos = []
        for carrera in self.data:
            for restaurant in carrera['restaurants']:
                for item in restaurant['items']:
                    price = round(float(item['price']) * 1.16, 2)
                    product = Producto(item['name'], item['type'], price)
                    productos.append(product)
        return productos
    def search(self, name=None, product_type=None, min_price=None, max_price=None):
        results = self.productos

        if name or product_type or min_price is not None or max_price is not None:
            if name:
                results = [p for p in results if name.lower() in p.name.lower()]
            if product_type:
                results = [p for p in results if product_type.lower() in p.product_type.lower()]
            if min_price is not None:
                results = [p for p in results if p.price >= min_price]
            if max_price is not None:
                results = [p for p in results if p.price <= max_price]
        else:
            print("Por favor, ingrese al menos un criterio de búsqueda.")
            return []

        return results


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
                
                results = self.search(name, product_type, min_price, max_price)

                if not results:
                    print('No se encontraron productos que coincidan con los criterios de búsqueda.')
                else:
                    print('Resultados de la búsqueda:')
                    for product in results:
                        print(product)
                        
            elif option == '2':
                print('Gracias por usar el sistema de gestión de restaurantes de carreras F1 VIP')
                menu_val=False
            else:
                print('Opción inválida, por favor intente de nuevo.')
