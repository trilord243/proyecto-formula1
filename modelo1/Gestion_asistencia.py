# Gestion_asistencia.py

class Gestion_Asistencia:
    def __init__(self):
        self.tokens = self.cargar_tokens()
    
    

    def cargar_tokens(self):
        try:
            with open("datos/tokens.txt", "r") as archivo_tokens:
                tokens = [line.strip().split(',') for line in archivo_tokens.readlines()]
                return tokens
        except FileNotFoundError:
            return []
    
    def obtener_info_token(self, token):
        for t in self.tokens:
            if t[0] == token:
                return t
        return None

    def token_existe(self, token):
        for t in self.tokens:
            if t[0] == token:
                return True
        return False

    def actualizar_asistencia(self, token, asistir):
        for i, t in enumerate(self.tokens):
            if t[0] == token:
                self.tokens[i][-1] = 'Asistirá' if asistir else 'No asistirá'
                break

    def guardar_tokens(self):
        with open("datos/tokens.txt", "w") as archivo_tokens:
            for token in self.tokens:
                archivo_tokens.write(','.join(token) + "\n")

    def start(self):
        token = input("Ingrese su token de entrada: ")
        token_info = self.obtener_info_token(token)

        if token_info is not None:
            print(f"¡Hola {token_info[1]}! ¿Vas a asistir?")
            respuesta = input("Responda con Si o No: ").lower()

            if respuesta == 'si':
                print("Gracias por confirmar tu asistencia.")
            elif respuesta == 'no':
                self.actualizar_asistencia(token, False)
                self.guardar_tokens()
                print("Asistencia actualizada a No asistirá.")
            else:
                print("Respuesta no válida. Por favor, responda con Si o No.")
        else:
            print("Token no encontrado. Por favor, verifique su token e intente nuevamente.")