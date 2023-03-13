import requests

class ApiPilotos:
    def __init__(self, url):
        self.url = url

    def obtener_pilotos(self):
        response = requests.get(self.url)
        return response.json()
