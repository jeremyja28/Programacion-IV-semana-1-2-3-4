class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones = []
        

    def asignar_calificacion(self, nota):
        self.calificaciones.append(nota)
    
    def mostrar_estudiante(self):
        print(f"Nombre: {self.nombre}")
        print(f"Matricula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        #Imprimir las calificaciones con su respesctiva materia
        if self.calificaciones:
            print("Calificaciones:")
            for i, calificacion in enumerate(self.calificaciones, 1):
                print(f"Materia #{i}: {calificacion['materia']} ---- Nota: {calificacion['nota']}")
    
    def mostrar_todos_estudiantes(self):
        print(f"Nombre: {self.nombre}")
        print(f"Matricula: {self.matricula}")
        print(f"Carrera: {self.carrera}")