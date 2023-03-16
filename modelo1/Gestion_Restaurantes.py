import json
import requests

class Gestion_Restaurante:
    def __init__(self):
        self.url = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        self.data = self.load_data()
        self.products = self.process_data()

    def load_data(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        return data

    def process_data(self):
        products = []
        for race in self.data:
            for restaurant in race['restaurants']:
                for item in restaurant['items']:
                    product = {
                        'name': item['name'],
                        'type': item['type'],
                        'price': round(float(item['price']) * 1.16, 2)
                    }
                    products.append(product)
        return products

    def search(self, name=None, product_type=None, min_price=None, max_price=None):
        results = self.products
        if name:
            results = [p for p in results if name.lower() in p['name'].lower()]
        if product_type:
            results = [p for p in results if product_type.lower() in p['type'].lower()]
        if min_price:
            results = [p for p in results if p['price'] >= min_price]
        if max_price:
            results = [p for p in results if p['price'] <= max_price]
        return results

    def start(self):
        print('Bienvenido al sistema de gestión de restaurantes de carreras F1 VIP')
        while True:
            print('1. Buscar productos')
            print('2. Salir')
            option = input('Seleccione una opción: ')
            if option == '1':
                name = input('Ingrese el nombre del producto (opcional): ')
                product_type = input('Ingrese el tipo de producto (opcional): ')
                min_price = input('Ingrese el precio mínimo (opcional): ')
                max_price = input('Ingrese el precio máximo (opcional): ')

                if min_price:
                    min_price = float(min_price)
                if max_price:
                    max_price = float(max_price)

                results = self.search(name, product_type, min_price, max_price)

                print('Resultados de la búsqueda:')
                for product in results:
                    print(f"Nombre: {product['name']}, Tipo: {product['type']}, Precio: {product['price']}")
            elif option == '2':
                print('Gracias por usar el sistema de gestión de restaurantes de carreras F1 VIP')
                break
            else:
                print('Opción inválida, por favor intente de nuevo.')




