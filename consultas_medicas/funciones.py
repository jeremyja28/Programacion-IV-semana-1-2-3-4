# Importamos la clase Paciente desde el archivo pacientes.py
from pacientes import Paciente

# Lista para almacenar a todos los pacientes registrados
lista_pacientes = []

# Lista de tipos de sangre disponibles
tipos_de_sangre = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# Función para registrar un nuevo paciente
def registrar_paciente():
    nombre = input("Nombre del paciente: ")
    while nombre == "":
        print("El nombre no puede estar vacio. ")
        nombre = input("Ingrese el nombre del paciente: ")

    # Validamos que la cédula sea numérica, de 10 dígitos y única
    while True:
        cedula = input("Cedula: ")
        if len(cedula) == 10 and cedula.isdigit():
            if cedula in [paciente.cedula for paciente in lista_pacientes]:
                print("La cédula ya está registrada. Ingrese una cédula diferente.")
            else:
                break
        else:
            print("La cédula debe tener 10 dígitos y ser numérica.")
    
    # Validamos que la edad sea un número mayor que cero
    while True:
        try:
            edad = int(input("Edad: "))
            if edad <= 0:
                print("La edad tiene que ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Edad invalida, ingrese de nuevo.")

    # Menú para seleccionar el tipo de sangre
    while True:
        print("Tipo de sangre: \n1. A+\n2. A-\n3. B+\n4. B-\n5. AB+\n6. AB-\n7. O+\n8. O-")
        try:
            opcion = int(input("Ingrese el tipo de sangre: "))
            if 1 <= opcion <= 8:
                tipo_de_sangre = tipos_de_sangre[opcion - 1]
                break
            else:
                print("Opción inválida. Debe ser un número entre 1 y 8.")
        except ValueError:
            print("Tipo de sangre inválido.")

    # Creamos el paciente y lo agregamos a la lista
    paciente_variable = Paciente(nombre, cedula, edad, tipo_de_sangre)
    lista_pacientes.append(paciente_variable)
    print("Paciente registrado con éxito.\n")

# Buscar un paciente por su cédula
def buscar_paciente(cedula):
    for paciente in lista_pacientes:
        if paciente.cedula == cedula:
            return paciente
    return None

# Agregar una consulta a un paciente existente
def agregar_consulta_paciente():
    while True:
        cedula_busqueda = input("Ingrese la cédula del paciente: ")
        if len(cedula_busqueda) == 10 and cedula_busqueda.isdigit():
            break
        else:
            print("La cédula debe tener 10 dígitos y ser numérica.")

    paciente = buscar_paciente(cedula_busqueda)
    if paciente:
        # Ingresar detalles de la consulta
        fecha = input("Ingrese la fecha de la consulta: ")
        diagnostico = input("Ingrese el diagnóstico: ")
        tratamiento = input("Ingrese el tratamiento: ")

        # Creamos un diccionario con los datos de la consulta
        diccionario_consulta = {
            "fecha": fecha,
            "diagnostico": diagnostico,
            "tratamiento": tratamiento
        }

        # Agregamos la consulta al paciente
        paciente.agregar_consulta(diccionario_consulta)
        print("Consulta registrada con éxito.\n")
    else:
        print("Paciente no encontrado.\n")

# Mostrar un paciente específico
def mostrar_paciente():
    while True:
        cedula_busqueda = input("Ingrese la cédula del paciente: ")
        if len(cedula_busqueda) == 10 and cedula_busqueda.isdigit():
            break
        else:
            print("La cédula debe tener 10 dígitos y ser numérica.")

    paciente = buscar_paciente(cedula_busqueda)
    if paciente:
        paciente.mostrar_datos()
    else:
        print("Paciente no encontrado.\n")

# Mostrar todos los pacientes registrados
def mostrar_todos():
    if not lista_pacientes:
        print("No hay pacientes registrados.")
    else:
        for paciente in lista_pacientes:
            paciente.mostrar_datos()
