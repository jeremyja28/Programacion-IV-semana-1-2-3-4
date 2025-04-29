# Importamos las funciones necesarias desde el archivo funciones.py
from funciones import registrar_paciente, agregar_consulta_paciente, mostrar_paciente, mostrar_todos
# Función que muestra el menú principal
def menu():
    while True:
        print("----- SISTEMA DE GESTIÓN DE CONSULTAS MÉDICAS -----")
        print("1. Registrar nuevo paciente")
        print("2. Agregar consulta a un paciente")
        print("3. Mostrar datos de un paciente")
        print("4. Mostrar todos los pacientes")
        print("5. Salir")
        # Solicitamos una opción al usuario
        opcion = input("Seleccione una opción: ")
        # Llamamos a la función correspondiente según la opción elegida
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            agregar_consulta_paciente()
        elif opcion == "3":
            mostrar_paciente()
        elif opcion == "4":
            mostrar_todos()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
# Ejecutamos el menú solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
    
    