#Llamando a las clases Apis
from apis.ApiCarreras import ApiCarreras
from apis.ApiConstructores import ApiConstructores
from apis.ApiPilotos import ApiPilotos
#Llamando a las clases del proyecto
from clases.Carrera import Carrera
from clases.Circuito import Circuito
from clases.Constructor import Constructor
from clases.Piloto import Piloto
import random


# Crear instancias de las APIs con sus respectivas clases y endpoints
api_constructores = ApiConstructores('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json')
api_pilotos = ApiPilotos('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json')
api_carreras = ApiCarreras('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')


# Lista de constructores registrados
constructores = []

# Lista de pilotos registrados
pilotos = []

# Lista de carreras registradas


# Lista de circuitos registrados
circuito = []


carreras = []







#Esta clase app contiene la aplicacion del modulo 1
class Gestion_carrera:
    
        
        
  
    
    
    
    
    
    #Funcion que registra los datos del api en el constructor.txt
    def registrar_constructores(self):
        #Llamando a las api de constructor 
        constructores_api = api_constructores.obtener_constructores()
        #Llamando a la api de los pilotos
        pilotos_api = api_pilotos.obtener_pilotos()
        
        #Creando y abriendo el txt de constructores.txt
        with open('datos/constructor.txt', 'w') as archivo:
            #Recorriendo el api constructores
            for constructor_api in constructores_api:
                #Extraer informacion del constructor    
                id_constructor = constructor_api["id"]
                name=constructor_api["name"]
                nationality=constructor_api["nationality"]
                
                 #Recorriendo el api pilotos y guardando los datos de la lista que corresponden al identificador del constructor
                team=[i["id"] for i in pilotos_api if constructor_api["id"]==i["team"]]
                
                #Asignandole valores a los atributos de la clase Constructor
                constructor = Constructor(id_constructor,name,nationality,team)
                #Guardo los datos en una lista constructorres
                constructores.append(constructor)
                #Esribiendo los datos en el archivo constructor.txt
                archivo.write(f"{constructor.nombre},{constructor.id},{constructor.nacionalidad}, {constructor.pilotos_ref[0]},{constructor.pilotos_ref[1]} \n")
                
                
    # Funcion que registra los datos del api en el pilotos.txt
    def registrar_pilotos(self):
        #Llamando el api de pilotos
        pilotos_api = api_pilotos.obtener_pilotos()
      
       #Creando y abriendo el txt de pilotos.txt
        with open('datos/pilotos.txt', 'w') as archivo:
            #Recorriendo el api de pilotos
            for piloto_api in pilotos_api:
                #Extraer informacion del piloto
                firstName=piloto_api['firstName']
                lastName=piloto_api['lastName']
                dateOfBirth=piloto_api['dateOfBirth']
                nationality=piloto_api['nationality']
                permanentNumber=piloto_api['permanentNumber']
                piloto_id=piloto_api['id']
                
                #Asignandole valores a los atributos
                piloto = Piloto(firstName, lastName, dateOfBirth, nationality, permanentNumber,piloto_id)
                #Guardo los datos en una lista pilotos
                pilotos.append(piloto)
                #Esribiendo los datos en el archivo pilotos.txt
                archivo.write(f"{piloto.nombre},{piloto.apellido},{piloto.fecha_nacimiento},{piloto.lugar_nacimiento},{piloto.numero},{piloto.id} \n")
            
    

    # Función para registrar carreras
    def registrar_carreras(self):
        #Llamando a las apis correspondientes
        carreras_api = api_carreras.obtener_carreras()
        
        #Creando y abriendo el txt de carreras.txt
        with open("datos/carreras.txt", "w") as archivo:
            #Recorriendo el api de carreras
            for carrera_api in carreras_api:
                # Extraer información de la carrera
                nombre = carrera_api['name']
                numero = carrera_api['round']
                fecha = carrera_api['date']
                id_carrera=carrera_api['circuit']["circuitId"]
                
                #Asignandole valores a los atributos
                carrera = Carrera(nombre, numero, fecha,id_carrera)
                #Guardo los datos en una lista carreras
                carreras.append(carrera)
                # Escribir los datos de la carrera en el archivo carreras.txt
                archivo.write(f"{carrera.nombre},{carrera.numero},{carrera.fecha},{carrera.circuito}\n")
        



   
   
   
    # Función para registrar circuitos
    def registrar_circuitos(self):
        #Llamando a las apis correspondientes
        circuitos_api=api_carreras.obtener_carreras()
        #Creando y abriendo el txt de carreras.txt
        with open("datos/circuitos.txt", "w") as archivo:
            #Recorriendo el api de carreras
            for circuito_api in circuitos_api:
                 # Extraer información de la carrera
                nombre=circuito_api['circuit']['name']
                pais=circuito_api['circuit']['location']['country']
                localidad=circuito_api['circuit']['location']['locality']
                latitud_longitud=[circuito_api['circuit']['location']['lat'],circuito_api['circuit']['location']['lat']]
                #Asignandole valores a los atributo
                circuitos=Circuito(nombre,pais,localidad,latitud_longitud)
                #Guardo los datos en una lista carreras
                circuito.append(circuitos)
                # Escribir los datos de la carrera en el archivo circuitos.txt
                archivo.write(f" {circuitos.nombre}, {circuitos.pais}, {circuitos.localidad}, {circuitos.latitud_longitud}\n")
            
            

    



 
    
  
    #Funcion que busca los constructores por pais. Donde recibe por parametro el pais
    def buscar_constructores_por_pais(self, pais):
        #Abrimos el archivo.txt que esta almacenado los datos de los constructores
        with open('datos/constructor.txt') as f:
            #Leer todas las lineas del constructor.txt y almacena una lista llamada lineas 
            lineas = f.readlines()
            #Se crea un booleano para un condicional
            constructores_encontrados = False
            #Recrirendo las lineas del constructor.txt
            for linea in lineas:
                #Toma la linea de codigo, elimina los espacios en blanco e indica la coma como separador
                constructor = linea.strip().split(',')
                #Si el pais que esta almacenado en el archivo.txt es igual al pais recibido por parametro Va a imprimir los datos de los constructores
                if constructor[2].lower() == pais.lower():
                    constructores_encontrados = True
                    print(f"Constructor: {constructor[0]}")
                    print(f"Alias: {constructor[1]}")
                    print(f"Pilotos: {constructor[3]} y {constructor[4]}")
                    print(" ")
            #Si no encuentra ningun constructor en el pais recibido por parametro imprime un mensaje
            if not constructores_encontrados:
                print(f"No se encontraron constructores en {pais}")





    def buscar_pilotos_por_constructor(self,a):
        #Creo una lista vacia para guardar los datos de los constructores
        constructor_dict = {}
        #Abro el archivo constructor.txt
        with open('datos/constructor.txt') as f:
            #Leer todas las lineas del constructor.txt y almacena una lista llamada
            lineas=f.readlines()
            
            for linea in lineas:
                constructor = linea.strip().split(',')
                #Se almacena los deatos del constructor en un diccionario en done el key es el nombre del constructor y el value es el nombre de los piloto
                constructor_dict[constructor[0]] = [constructor[3],constructor[4]]

        #Recorro el diccionario para encontrar los datos de los pilotos
        for key,value in constructor_dict.items():
            #Si el key del diccionario es igual al nombre del parametro recibido entonces se abre el archivo pilotos.txt
            if key==a:
                with open('datos/pilotos.txt') as f:
                    lineas=f.readlines()
                    for lineas in lineas:
                        pilotos = lineas.strip().split(',')
                        #Si el valor del diccionario es igual al piloto del value que estan registradors los pilotos del diccionario entonces se imprime los valores del pilotos que se estan buscando 
                        if pilotos[5] in value[0]:
                            print(f"""Piloto1 
                                  
                                 nombre: {pilotos[0]} 
                                 apellido: {pilotos[1]}
                                 fecha de nacimiento: {pilotos[2]}
                                 nacionalidad: {pilotos[3]}
                                  """ )
                            #Se imprime los datos de otro piloto que esta en esa lista 
                        if pilotos[5] in value[1]:
                             print(f"""Piloto2
                                 nombre: {pilotos[0]} 
                                 apellido: {pilotos[1]}
                                 fecha_nacimiento: {pilotos[2]}
                                 nacionalidad: {pilotos[3]}
                                  """ )
    def imprimir_pilotos(self):
        mensaje = """\n Bienvenido, aqui esta la lista de paises disponibles para buscar los constructores
            Selecione el numero del pais o escriba pais exactamente como se te esta dando 
        \n """
        print(mensaje)
        dict_construcores_numero = {}
        with open('datos/constructor.txt') as f:
            contador = 0
            #Leer todas las lineas del constructor.txt y almacena una lista llamada
            lineas=f.readlines()
            
            for linea in lineas:
                contador += 1
                constructor = linea.strip().split(',')
                
                dict_construcores_numero[contador]=constructor[0]
        for key ,value in dict_construcores_numero.items():
            print(f"{key}. {value}")
        
        opcion = input("Ingrese el numero del pais o el nombre del pais: ")
        data = opcion
        for key, value in dict_construcores_numero.items():
            #Si la opcion es un digito enonces se le asigna el KEW a la data y se comprueba si es un digito 
            if opcion.isdigit() and int(opcion) == key:
                data = key
                break
            #Si la opcion no es un digito entonces se le asigna el valor Key de esa opcion de esa data
            elif opcion.lower() == value.lower():
                data = key
                break
        
        if type(data) == int:
            return dict_construcores_numero[data]
        elif type(data) == str:
            return data
            
         
    #Funcion que busca las carreras por pais. Donde recibe por parametro el pais 
    def buscar_carreras_por_pais(self,pais):
        #Se llama a la api de carreras 
        carreras_dict=api_carreras.obtener_carreras()
        #Se recorre el diccionario para encontrar las carreras
        for i in range(len(carreras_dict)):
            #Si El pais recibido por parametro es igual al pais de la carrera Entonces imprime los datos de la carrera
            if carreras_dict[i]["circuit"]['location']['country'].lower() == pais.lower():
                
                print(f"Carrera: {carreras_dict[i]['circuit']['name']}")
                
                print(f"Localidad: {carreras_dict[i]['circuit']['location']['locality']}")
                print(f"Latitud: {carreras_dict[i]['circuit']['location']['lat']}")
                print(f"Longitud: {carreras_dict[i]['circuit']['location']['long']}")
                
    def imprimir_carreras(self):
        carreras_dict=api_carreras.obtener_carreras()
        dict_carreras = {}
        contador=0
        for i in range(len(carreras_dict)):
            contador+=1
            dict_carreras[contador]=carreras_dict[i]["circuit"]['location']['country']
        for key, value in dict_carreras.items():
                print(f"{key}. {value}")
            
        opcion = input("Ingrese el numero del pais o el nombre del pais: ")
        data = opcion
        
        #Recorriendo el diccionario para 
        for key, value in dict_carreras.items():
            #Si la opcion es un digito enonces se le asigna el KEW a la data y se comprueba si es un digito 
            if opcion.isdigit() and int(opcion) == key:
                data = key
                break
            #Si la opcion no es un digito entonces se le asigna el valor Key de esa opcion de esa data
            elif opcion.lower() == value.lower():
                data = key
                break
        
        if type(data) == int:
            return dict_carreras[data]
        elif type(data) == str:
            return data
        
        
            
            
        
        
    #Funcion que busca los datos de la carrera por mes. Que recibe por parametro el mes
    def buscar_carreras_por_mes(self,mes):
        #Llamar el api de carreras
        carreras_dict=api_carreras.obtener_carreras()
        
        
        #Recorrer la lista de carreras
        for i in range(len(carreras_dict)):
            partes=carreras_dict[i]['date'].split('-')
            #Si el mes recibido por parametro es igual al mes de la carrera Entonces imprime los datos de la carrera
            
            if int(partes[1])==mes:
                
                
                print(f"""
                    Carrera: 
                    
                    carrera: {carreras_dict[i]['name']}
                    circuito: {carreras_dict[i]['circuit']['name']}
                    location: {carreras_dict[i]['circuit']['location']['locality']}
                      
                      
                
                      """)
            elif int(partes[1])!=mes:
                print("No existe la carrera")
                break
            
            
                
    
    def imprimir_meses(self):
        print("""
            \n Escoja el mes de la carrera que deseas imprimir:
        1. Enero
        2. Febrero
        3. Marzo
        4. Abril
        5. Mayo
        6. Junio
        7. Julio
        8. Agosto
        9. Septiembre
        10. Octubre
        11. Noviembre
        12. Diciembre   
            """)

        validacion_mes = True
        while validacion_mes:

            opcion = input("Ingrese el numero del mes: ")
            if opcion.isdigit():
                opcion_int = int(opcion)
                if opcion_int in range(1, 13):
                    validacion_mes = False
                else:
                    print("Ingrese un número válido del 1 al 12.")
            else:
                print("Ingrese solo dígitos.")

        return opcion_int

                
               
        
        
        
        
            
      
    
    
            
         

    #Imprime los paises dispobibles
    def imprimir_paises(self):
        mensaje = """\n Bienvenido, aqui esta la lista de paises disponibles para buscar los constructores
            Selecione el numero del pais o escriba pais exactamente como se te esta dando 
        \n """
        print(mensaje)
        #Creando un diccionarrio para guardar los pais
        dict_paises_numero = {}
        #Abriendo el constructor.txt para sacar los paises disponibles
        with open('datos/constructor.txt') as f:
            lineas = f.readlines()
            contador = 0
            for linea in lineas:
                #Contador para asignarle un numero a cada pais
                contador += 1
                constructor = linea.strip().split(',')
                #Creando la lista nueva para guardar los datos de los paises y el numero de cada pais 
                dict_paises_numero[contador] = constructor[2]
        #Imprimir la lista para que los usuario pueda seleccionar los datos mas facilmente 
        for key, value in dict_paises_numero.items():
            print(f"{key}. {value}")
        
        opcion = input("Ingrese el numero del pais o el nombre del pais: ")
        data = opcion
        
        #Recorriendo el diccionario para 
        for key, value in dict_paises_numero.items():
            #Si la opcion es un digito enonces se le asigna el KEW a la data y se comprueba si es un digito 
            if opcion.isdigit() and int(opcion) == key:
                data = key
                break
            #Si la opcion no es un digito entonces se le asigna el valor Key de esa opcion de esa data
            elif opcion.lower() == value.lower():
                data = key
                break
        
        if type(data) == int:
            return dict_paises_numero[data]
        elif type(data) == str:
            return data
        
    def finalizar_carrera(self,carrera_numero):
        # Selecciona 10 pilotos al azar y les asigna una posición
        pilotos_seleccionados = random.sample(pilotos, 10)
        pilotos_seleccionados.sort(key=lambda x: x.puntos, reverse=True)

        # Asigna puntos a los pilotos según su posición
        puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        for i, piloto in enumerate(pilotos_seleccionados):
            piloto.agregar_puntos(puntos[i])
            piloto.guardar_datos()

            # Encuentra y actualiza el constructor al que pertenece el piloto
            for constructor in constructores:
                if piloto.id in constructor.pilotos_ref:
                    constructor.agregar_puntos(puntos[i])
                    constructor.guardar_datos()
        
        for carrera in carreras:
            if carrera.numero == carrera_numero:
                carrera.podium = [piloto.id for piloto in pilotos_seleccionados[:3]]
                carrera.guardar_datos()

        # Imprime el podio
        print("Podio:")
        for i in range(3):
            print(f"{i + 1}. {pilotos_seleccionados[i].nombre} {pilotos_seleccionados[i].apellido} - {puntos[i]} puntos")   
       
       
       
    def start(self):
        menu_val = True
        volver_al_menu_principal = False
        while menu_val:
            self.registrar_constructores()
            self.registrar_pilotos()
            self.registrar_carreras()
            self.registrar_circuitos()
            print("Bienvenido al primer modulo del programa de Formula 1 !\n")
            print("Seleccione una opcion para lo que desea realizar:\n")
            print("1. Buscar constructores por país")
            print("2. Buscar pilotos por constructor")
            print("3. Buscar carreras por país")
            print("4. Buscar carreras por mes")
            print("5. Finalizar carrera y asignar puntos")
            
            opcion=input("Escriba la opcion: ")
            if opcion=="1":
                pais=self.imprimir_paises()
                self.buscar_constructores_por_pais(pais)
            elif opcion=="2":
                pilotos=self.imprimir_pilotos()
                self.buscar_pilotos_por_constructor(pilotos)
            elif opcion=="3":
                carreras=self.imprimir_carreras()
                self.buscar_carreras_por_pais(carreras)
            elif opcion=="4":
                mes=self.imprimir_meses()
                self.buscar_carreras_por_mes(mes)
            elif opcion == "5":
                carrera_numero = input("Ingrese el número de la carrera a finalizar: ")
                while not carrera_numero.isdigit():
                    carrera_numero=input("Ingrese un valor numerico: ")
                data=int(carrera_numero)
                self.finalizar_carrera(data)
            else:
                print("Opción no válida. Regresando al menú principal.")
                menu_val = False
                volver_al_menu_principal = True  

        return volver_al_menu_principal  # Asegurarse de que el 'return' esté fuera del bucle 'while'

                    
                
                
                
            
            
            
            
        
        
        
