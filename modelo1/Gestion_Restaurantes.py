import requests
import json

class Gestion_Restaurantes:

    def __init__(self):
        self.url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        self.restaurantes = self.obtener_restaurantes()

    def obtener_restaurantes(self):
        try:
            response = requests.get(self.url)
            data = json.loads(response.text)
            return data['races'][0]['restaurants']
        except Exception as e:
            print(f"Error al obtener los restaurantes: {e}")
            return []

    def verificar_cliente_vip(self, cedula):
        with open('datos/tokens.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                token_info = line.strip().split(',')
                if token_info[2] == cedula and token_info[4] == 'vip':
                    return True
        return False

    # Otros métodos

def main():
    gestion_restaurantes = Gestion_Restaurantes()
    # Código para interactuar con el usuario

if __name__ == "__main__":
    main()
