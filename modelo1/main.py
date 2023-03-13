
#Llamando clases de apis
from apis.ApiCarreras import ApiCarreras
from apis.ApiConstructores import ApiConstructores
from apis.ApiPilotos import ApiPilotos
#Llamando a las clases del proyecto
from clases.Carrera import Carrera
from clases.Circuito import Circuito
from clases.Constructor import Constructor
from clases.Piloto import Piloto


# Crear instancias de las APIs
api_constructores = ApiConstructores('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json')
api_pilotos = ApiPilotos('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json')
api_carreras = ApiCarreras('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')

# Lista de constructores registrados
constructores = []

# Lista de pilotos registrados
pilotos = []

# Lista de carreras registradas


# Lista de circuitos registrados
circuitos = []

# Función para registrar constructores
def registrar_constructores():
    
    
    
    constructores_api = api_constructores.obtener_constructores()
    pilotos_api = api_pilotos.obtener_pilotos()
    
    for constructor_api in constructores_api:
        team=[i["id"] for i in pilotos_api if constructor_api["id"]==i["team"]]
        
        
        constructor = Constructor(constructor_api['id'], constructor_api['name'], constructor_api['nationality'],team)
        constructores.append(constructor)
    with open('constructor.txt', 'w') as archivo:
        # Escribir la información de cada piloto en el archivo
        for constructor in constructores:
            archivo.write(f" [ {constructor.nombre},{constructor.id},{constructor.nacionalidad}, {constructor.pilotos_ref} ] \n")

# Función para registrar pilotos
def registrar_pilotos():
    pilotos_api = api_pilotos.obtener_pilotos()
    for piloto_api in pilotos_api:
        piloto = Piloto(piloto_api['firstName'], piloto_api['lastName'], piloto_api['dateOfBirth'], piloto_api['nationality'], piloto_api['permanentNumber'])
        pilotos.append(piloto)
    
    # Abrir el archivo de texto en modo escritura
    with open('pilotos.txt', 'w') as archivo:
        # Escribir la información de cada piloto en el archivo
        for piloto in pilotos:
            archivo.write(f"[{piloto.nombre},{piloto.apellido},{piloto.fecha_nacimiento},{piloto.lugar_nacimiento},{piloto.numero}]\n")
           
            
    print("Se ha creado el archivo 'pilotos.txt' con la información de los pilotos registrados.")

    
    
    
   






# Función para registrar carreras


def registrar_carreras():
    carreras_api = api_carreras.obtener_carreras()
    carreras = []
    with open("carreras.txt", "w") as archivo:
        for carrera_api in carreras_api:
            # Extraer información de la carrera
            nombre = carrera_api['name']
            numero = carrera_api['round']
            fecha = carrera_api['date']
            circuito_api = carrera_api['circuit']
            circuito = Circuito(circuito_api['name'], circuito_api['location']['country'], circuito_api['location']['locality'], circuito_api['location']['lat'], circuito_api['location']['long'])
            podium = []
            carrera = Carrera(nombre, numero, fecha, circuito, podium)
            carreras.append(carrera)
            # Escribir los datos de la carrera en el archivo
            archivo.write(f"{carrera.nombre}, {carrera.numero}, {carrera.fecha}, {carrera.circuito.nombre}, {carrera.circuito.pais}, {carrera.circuito.localidad}, {carrera.circuito.latitud}, {carrera.circuito.longitud}\n")
    return carreras



# Función para registrar circuitos


def registrar_circuitos():
    circuitos_api = api_carreras.obtener_carreras()
    circuitos = []
    for circuito_api in circuitos_api:
        # Extraer información del circuito
        nombre = circuito_api['name']
        pais = circuito_api['location']['country']
        localidad = circuito_api['location']['locality']
        latitud = circuito_api['location']['lat']
        longitud = circuito_api['location']['long']
        circuito = Circuito(pais, localidad, latitud, longitud, nombre, circuito_api['circuitId'])
        circuitos.append(circuito)

    return circuitos




 
# Función para buscar constructores por país
def buscar_constructores_por_pais():
    pais = input("Ingrese el país del constructor a buscar: ")
    constructores_pais = [x for x in constructores if x.nacionalidad == pais]
    for constructor in constructores_pais:
        print(f"ID: {constructor.id} - Nombre: {constructor.nombre}")

# Función para buscar pilotos por constructor
def buscar_pilotos_por_constructor():
    constructor_id = input("Ingrese el ID del constructor: ")
    constructor = next((x for x in constructores if x.id == constructor_id), None)
    if constructor:
        pilotos_constructor = constructor.pilotos
        for piloto in pilotos_constructor:
            print(f"Nombre: {piloto.nombre} {piloto.apellido} - Número: {piloto.numero}")
        else:
            print("No se encontró el constructor")
            
def buscar_carreras_por_pais_circuito():
    pais = input("Ingrese el país del circuito a buscar: ")
    carreras_pais = [x for x in carreras if x.circuito.pais == pais]
    for carrera in carreras_pais:
        print(f"Número: {carrera.numero} - Nombre: {carrera.nombre}")
        
        

while True:
    print("Seleccione una opción:")
    print("1. Registrar constructores")
    print("2. Registrar pilotos")
    print("3. Registrar carreras")
    print("4. Registrar circuitos")
    print("5. Buscar constructores por país")
    print("6. Buscar pilotos por constructor")
    print("7. Buscar carreras por país del circuito")
    print("8. Buscar carreras por mes")
    print("9. Finalizar carrera")
    print("10. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        registrar_constructores()
    elif opcion == "2":
        registrar_pilotos()
    elif opcion == "3":
        registrar_carreras()
    elif opcion == "4":
        registrar_circuitos()
    elif opcion == "5":
        buscar_constructores_por_pais()
    elif opcion == "6":
        buscar_pilotos_por_constructor()
    elif opcion == "7":
        buscar_carreras_por_pais_circuito()
    else:
    
        print("Opción inválida") 