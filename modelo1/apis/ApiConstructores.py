#Se importa el modulo para llamar las apis
import requests
#Se crea la clase que recibe la url de la api y luego con su metodo obtener carreras obtiene los datos de la api
class ApiConstructores:
    def __init__(self, url):
        self.url = url

    def obtener_constructores(self):
        response = requests.get(self.url)
        return response.json()
