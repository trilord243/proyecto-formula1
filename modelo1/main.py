
#Se importa la clase App que contiene la funcionalidad del programa
from Gestion_Carrera import Gestion_carrera

from Venta_entradas import Venta_entradas

#Se crea una funcion main que se ejecuta cuando se ejecuta el programa
def main():
    menu_principal = True
    while menu_principal:
        print("Bienvenido a todos! ")
        print("1. Gestionar carreras")
        print("venta de entradas")
        opcion = input("Escoge una opcion: ")
        if opcion == "1":
            volver_al_menu_principal = Gestion_carrera().start()
            if not volver_al_menu_principal:
                menu_principal = False
        elif opcion == "2":
            Venta_entradas().start()
        else:
            print("Opción no válida")
            menu_principal = False

# Se ejecuta el programa
main()
