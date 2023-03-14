#Se importa el modulo para llamar las apis
import requests
#Se crea la clase que recibe la url de la api y luego con su metodo obtener carreras obtiene los datos de la api
class ApiCarreras:
    def __init__(self, url):
        self.url = url

    def obtener_carreras(self):
        response = requests.get(self.url)
        return response.json()
