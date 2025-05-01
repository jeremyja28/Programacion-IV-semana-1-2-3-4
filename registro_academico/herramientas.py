from estudiante import Estudiante

lista_estudiantes = []

def registrar_estudiante():
    while True:
        nombre = input("Nombre del estudiante: ")
        if nombre.strip() != "":
            break
        print("El nombre no puede estar vacio.")
    while True:
        matricula = input("Matricula (debe contener 10 numeros): ")
        if len(matricula) == 10 and matricula.isdigit():
            if matricula in [estudiante.matricula for estudiante in lista_estudiantes]:
                print("La matricula ya esta registrada. Ingrese una matricula diferente.")
            else:
                break
        else:
            print("La matricula debe tener 10 digitos y ser numerica.")
    while True:
        carrera = input("Carrera: ")
        if carrera.strip() != "":
            break
        print("La carrera no puede estar vacia.")
    
    estudiante_variable = Estudiante(nombre, matricula, carrera)
    lista_estudiantes.append(estudiante_variable)
    print("Estudiante registrado con exito.\n")
    
    
def busqueda_estudiante(matricula):
    for estudiante in lista_estudiantes:
        if estudiante.matricula == matricula:
            return estudiante
    return None

def asignar_calificacion_estudiante():
    matricula_busqueda = input("Ingrese la matricula del estudiante: ")
    estudiante = busqueda_estudiante(matricula_busqueda)
    if estudiante:
        while True:
            materia = input("Materia: ")
            if materia.strip() != "":
                break
            print("La materia no puede estar vacia.")
        while True:
            try:
                nota = float(input("Nota: "))
                if 0 <= nota <= 10:
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
                    
            except ValueError:
                print("Nota invalida.")
        diccionario_calificacion = {
            "materia": materia,
            "nota" : nota
        }
        estudiante.asignar_calificacion(diccionario_calificacion)
        print("Calificacion asignada con exito.\n")
    else:
        print("No se encontro el estudiante con la matricula ingresada.\n")

def mostrar_estudiante():
    matricula_busqueda = input("Ingrese la matricula del estudiante: ")
    estudiante = busqueda_estudiante(matricula_busqueda)
    if estudiante:
        estudiante.mostrar_estudiante()
    else:
        print("No se encontro el estudiante con la matricula ingresada.\n")

def mostrar_todos_estudiantes():
    if lista_estudiantes:
        for estudiante in lista_estudiantes:
            estudiante.mostrar_todos_estudiantes()
    else:
        print("No hay estudiantes registrados.\n")


    