


#Clase de Gestion de asistencia 
class Gestion_Asistencia:
    def __init__(self):
        self.tokens = self.cargar_tokens()
    
    
    #Metodo que guarda todos los tokens en una lista 
    def cargar_tokens(self):
        #Si no existe ningun token entonces entonces da un error ya que solo tiene permisos de lecttura "r"
        try:
            with open("datos/tokens.txt", "r") as archivo_tokens:
                #Se guarda en una lista los tokens gracias al list compregension y sera una lista de listas 
                tokens = [line.strip().split(',') for line in archivo_tokens.readlines()]
                return tokens
        except FileNotFoundError:
            #Si no te sencuentra ningun archivo retorna una lista vacia 
            return []
    
    #Metodo que para verificar si el token entregado por el usuario es valido 
    def obtener_info_token(self, token):
        #Se itera sobre los tokens para verificar si el token es valido 
        for t in self.tokens:
            if t[0] == token:
                #Si es valido entonces se devuelve la informacion del token 
                return t
        #Si no es valido entonces retorna None
        return None


    #Metodo para actualizar la asistencia  de un usuario 
    def actualizar_asistencia(self, token, asistir):
        #Se iteral la informacion del token
        for i, t in enumerate(self.tokens):
            #Si el token es igual al token que entregamos por el usuario 
            if t[0] == token:
                #Si el usuario por parametro No asistira entonces se actualiza la asistencia 
                self.tokens[i][-1] = 'Asistirá' if asistir else 'No asistirá'
                break
    #Metodo que actualiza el txt de tokes 
    def guardar_tokens(self):
        #Se abre el txt de tokes 
        with open("datos/tokens.txt", "w") as archivo_tokens:
            #Por cada iteracion de self.tokens va a acutalizar los datos que el tenga si no tiene nuingun cambio entonces se dejara igual 
            for token in self.tokens:
                archivo_tokens.write(','.join(token) + "\n")

    #Metodo que inicializa el modulo 
    def start(self):
        #Ingresa el token por por usuario 
        token = input("Ingrese su token de entrada: ")
        #Se le pasa por parametro el token al obtener la informacion del token 
        token_info = self.obtener_info_token(token)
        #Si el metodo retorna algo diferente de None entonces podra actualizar su asitencia
        if token_info is not None:
            
            print(f"¡Hola {token_info[1]}! ¿Vas a asistir?")
            respuesta = input("Responda con Si o No: ").lower()

            if respuesta == 'si':
                #Si la respuesta es si entonces no hace nada 
                print("Gracias por confirmar tu asistencia.")
            #Si la respuesta es no entonces va a actualizar la asistenca con el metodo actualizar_asistencia 
            elif respuesta == 'no':
                self.actualizar_asistencia(token, False)
                self.guardar_tokens()
                print("Asistencia actualizada a No asistirá.")
            else:
                print("Respuesta no válida. Por favor, responda con Si o No.")
        else:
            print("Token no encontrado. Por favor, verifique su token e intente nuevamente.")