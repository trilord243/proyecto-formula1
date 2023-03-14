#Llamando a las clases Apis
from apis.ApiCarreras import ApiCarreras
from apis.ApiConstructores import ApiConstructores
from apis.ApiPilotos import ApiPilotos
#Llamando a las clases del proyecto
from clases.Carrera import Carrera
from clases.Circuito import Circuito
from clases.Constructor import Constructor
from clases.Piloto import Piloto
import json

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

# Clase de la funcion principal



class App:

    def registrar_constructores(self):
        #Llamando a las apis correspondientes
        constructores_api = api_constructores.obtener_constructores()
        pilotos_api = api_pilotos.obtener_pilotos()
        
        #Creando y abriendo el txt de constructores
        with open('constructor.txt', 'w') as archivo:
            #Recorriendo el api constructores
            for constructor_api in constructores_api:
                #Extraer informacion del constructor    
                id_constructor = constructor_api["id"]
                name=constructor_api["name"]
                nationality=constructor_api["nationality"]
                
                 #Recorriendo el api pilotos y guardando los datos de la lista que corresponden al identificador del constructor
                team=[i["id"] for i in pilotos_api if constructor_api["id"]==i["team"]]
                
                #Asignandole valores a los atributos
                constructor = Constructor(id_constructor,name,nationality,team)
                #Guardo los datos en una lista para guardarlos en el archivo.txt
                constructores.append(constructor)
                archivo.write(f"{constructor.nombre},{constructor.id},{constructor.nacionalidad}, {constructor.pilotos_ref[0]},{constructor.pilotos_ref[1]} \n")
                
                
    # Función para registrar pilotos
    def registrar_pilotos(self):
        #Llamando a las apis correspondientes
        pilotos_api = api_pilotos.obtener_pilotos()
      
       #Creando y abriendo el txt de pilotos
        with open('pilotos.txt', 'w') as archivo:
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
                pilotos.append(piloto)
                archivo.write(f"{piloto.nombre},{piloto.apellido},{piloto.fecha_nacimiento},{piloto.lugar_nacimiento},{piloto.numero},{piloto.id} \n")
            
    

    # Función para registrar carreras
    def registrar_carreras(self):
        #Llamando a las apis correspondientes
        carreras_api = api_carreras.obtener_carreras()
        carreras = []
        #Creando y abriendo el txt de carreras
        with open("carreras.txt", "w") as archivo:
            #Recorriendo el api de carreras
            for carrera_api in carreras_api:
                # Extraer información de la carrera
                nombre = carrera_api['name']
                numero = carrera_api['round']
                fecha = carrera_api['date']
                id_carrera=carrera_api['circuit']["circuitId"]
                
                #Asignandole valores a los atributos
                carrera = Carrera(nombre, numero, fecha,id_carrera)
                carreras.append(carrera)
                # Escribir los datos de la carrera en el archivo
                archivo.write(f"{carrera.nombre},{carrera.numero},{carrera.fecha},{carrera.circuito}\n")
        return carreras



   
   
   
    # Función para registrar circuitos
    def registrar_circuitos(self):
        circuitos_api=api_carreras.obtener_carreras()
        with open("circuitos.txt", "w") as archivo:
            for circuito_api in circuitos_api:
                nombre=circuito_api['circuit']['name']
                pais=circuito_api['circuit']['location']['country']
                localidad=circuito_api['circuit']['location']['locality']
                latitud_longitud=[circuito_api['circuit']['location']['lat'],circuito_api['circuit']['location']['lat']]
                circuitos=Circuito(nombre,pais,localidad,latitud_longitud)
                circuito.append(circuitos)
                archivo.write(f" {circuitos.nombre}, {circuitos.pais}, {circuitos.localidad}, {circuitos.latitud_longitud}\n")
            
            return circuito

    
    #Funcion para filtrar por constructor, recibe el pais y te entrega los datos de los constructores con ese pais 


 
    
  

    def buscar_constructores_por_pais(self, pais):
        with open('constructor.txt') as f:
            lineas = f.readlines()
            constructores_encontrados = False
            for linea in lineas:
                constructor = linea.strip().split(',')
                if constructor[2].lower() == pais.lower():
                    constructores_encontrados = True
                    print(f"Constructor: {constructor[0]}")
                    print(f"Alias: {constructor[1]}")
                    print(f"Pilotos: {constructor[3]} y {constructor[4]}")
                    print()
            if not constructores_encontrados:
                print(f"No se encontraron constructores en {pais}")





    def buscar_pilotos_por_constructor(self,a):
        constructor_dict = {}
        with open('constructor.txt') as f:
            lineas=f.readlines()
            for linea in lineas:
                constructor = linea.strip().split(',')
                constructor_dict[constructor[0]] = [constructor[3],constructor[4]]
        
        for key,value in constructor_dict.items():
            if key==a:
                with open('pilotos.txt') as f:
                    lineas=f.readlines()
                    for lineas in lineas:
                        pilotos = lineas.strip().split(',')
                        if pilotos[5] in value[0]:
                            print(f"""Piloto1 
                                  
                                 nombre: {pilotos[0]} 
                                 apellido: {pilotos[1]}
                                 fecha de nacimiento: {pilotos[2]}
                                 nacionalidad: {pilotos[3]}
                                 
                                  
                                  
                                  
                                  """ )
                        if pilotos[5] in value[1]:
                             print(f"""Piloto2
                                  
                                 nombre: {pilotos[0]} 
                                 apellido: {pilotos[1]}
                                 fecha_nacimiento: {pilotos[2]}
                                 nacionalidad: {pilotos[3]}
                                 
                                  
                                  
                                  
                                  """ )
    
                         
            
        
  
           
    def buscar_carreras_por_pais(self,pais):
        carreras_dict=api_carreras.obtener_carreras()
        
        for i in range(len(carreras_dict)):
           
            if carreras_dict[i]["circuit"]['location']['country'].lower() == pais.lower():
                
                print(f"Carrera: {carreras_dict[i]['circuit']['name']}")
                
                print(f"Localidad: {carreras_dict[i]['circuit']['location']['locality']}")
                print(f"Latitud: {carreras_dict[i]['circuit']['location']['lat']}")
                print(f"Longitud: {carreras_dict[i]['circuit']['location']['long']}")
                
           
    
    def buscar_carreras_por_mes(self,mes):
        carreras_dict=api_carreras.obtener_carreras()
        print(f"\nEn el mes {mes} daran estas carreras:")
        for i in range(len(carreras_dict)):
            partes=carreras_dict[i]['date'].split('-')
            if int(partes[1])==mes:
                print(f"""
                    
                    
                    carrera: {carreras_dict[i]['name']}
                    circuito: {carreras_dict[i]['circuit']['name']}
                    location: {carreras_dict[i]['circuit']['location']['locality']}
                      
                      
                      
                      
                      
                      """)
            
         

                    

    
    

    def start(self):
        self.registrar_constructores()
        self.registrar_pilotos()
        self.registrar_carreras()
        self.registrar_circuitos()
        
        
