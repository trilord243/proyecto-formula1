import requests

class ApiCarreras:
    def __init__(self, url):
        self.url = url

    def obtener_carreras(self):
        response = requests.get(self.url)
        return response.json()
