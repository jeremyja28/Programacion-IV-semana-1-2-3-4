# Importamos las funciones necesarias desde el archivo utilidades.py
from herramientas import registrar_estudiante, asignar_calificacion_estudiante, mostrar_estudiante, mostrar_todos_estudiantes
# Función que muestra el menú principal
def menu():
    while True:
        print("----- SISTEMA DE REGISTRO ACADÉMICO -----")
        print("1. Registrar nuevo estudiante")
        print("2. Registrar calificación de un estudiante")
        print("3. Mostrar datos de un estudiante")
        print("4. Mostrar todos los estudiantes registrados")
        print("5. Salir")
        # Solicitamos una opción al usuario
        opcion = input("Seleccione una opción: ")
        # Llamamos a la función correspondiente según la opción elegida
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            asignar_calificacion_estudiante()
        elif opcion == "3":
            mostrar_estudiante()
        elif opcion == "4":
            mostrar_todos_estudiantes()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
# Ejecutamos el menú solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
    
    