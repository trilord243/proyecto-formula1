import requests

class ApiConstructores:
    def __init__(self, url):
        self.url = url

    def obtener_constructores(self):
        response = requests.get(self.url)
        return response.json()
