
#Se importa la clase App que contiene la funcionalidad del programa
from Gestion_Carrera import Gestion_carrera
from Gestion_asistencia import Gestion_Asistencia
from Venta_entradas import Venta_entradas
from Gestion_Restaurantes import Gestion_Restaurante
from Ventas_Restaurantes import Ventas_Restaurantes

#Se crea una funcion main que se ejecuta cuando se ejecuta el programa
def main():
    menu_principal = True
    while menu_principal:
        print("Bienvenido a todos! ")
        print("1. Gestionar carreras")
        print("2.venta de entradas")
        print("3.Gestion_asistencia ")
        print("4.Gestion_Restaurantes")
        print("5. Ventas Restaurante")
        opcion = input("Escoge una opcion: ")
        if opcion == "1":
            volver_al_menu_principal = Gestion_carrera().start()
            if not volver_al_menu_principal:
                menu_principal = False
        elif opcion == "2":
            Venta_entradas().start()
        elif opcion == "3":
            Gestion_Asistencia().start()
        elif opcion=="4":
            Gestion_Restaurante().start()
        elif opcion == "5":
            Ventas_Restaurantes().start()
        elif opcion == "6":
            print("UWUWUWWU")
            
            
        else:
            print("Opción no válida")
            menu_principal = False

# Se ejecuta el programa
main()
