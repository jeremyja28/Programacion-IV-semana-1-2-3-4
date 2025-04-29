# Clase Paciente que guarda los datos y las consultas médicas
class Paciente:
    def __init__(self, nombre, cedula, edad, tipo_de_sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_de_sangre = tipo_de_sangre
        self.consulta = []  # Lista de diccionarios con las consultas
    
    # Agrega una nueva consulta al paciente
    def agregar_consulta(self, datos_consulta):
        self.consulta.append(datos_consulta)
    
    # Muestra todos los datos del paciente y sus consultas
    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de Sangre: {self.tipo_de_sangre}")
        
        if not self.consulta:
            print("Consultas: No tiene consultas registradas.")
        else:
            print("Consultas:")
            for i, consulta in enumerate(self.consulta, 1):
                print(f"  Consulta #{i}:")
                print(f"    Fecha: {consulta['fecha']}")
                print(f"    Diagnóstico: {consulta['diagnostico']}")
                print(f"    Tratamiento: {consulta['tratamiento']}")
        print()  # Espacio extra al final
