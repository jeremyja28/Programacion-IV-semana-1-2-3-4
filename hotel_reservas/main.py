# Importamos las funciones necesarias desde el archivo utilidades.py
from utilidades import registrar_huesped, agregar_reserva_huesped, mostrar_reservas_huespedes, mostrar_huespedes_registrados
# Función que muestra el menú principal
def menu():
    while True:
        print("----- SISTEMA DE GESTIÓN DE RESERVAS DE UN HOTEL -----")
        print("1. Registrar nuevo huesped")
        print("2. Crear reserva de un huesped")
        print("3. Mostrar todas las reservas")
        print("4. Mostrar todos los huespedes registrados")
        print("5. Salir")
        # Solicitamos una opción al usuario
        opcion = input("Seleccione una opción: ")
        # Llamamos a la función correspondiente según la opción elegida
        if opcion == "1":
            registrar_huesped()
        elif opcion == "2":
            agregar_reserva_huesped()
        elif opcion == "3":
            mostrar_reservas_huespedes()
        elif opcion == "4":
            mostrar_huespedes_registrados()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
# Ejecutamos el menú solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
    
    