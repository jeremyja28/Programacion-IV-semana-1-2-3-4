from huesped import Huesped

#Lista de huespedes registrados
lista_huespedes = []
#Lista de tipos de habitaciones disponibles
tipos_de_habitaciones = ["Individual", "Doble", "Suite", "Familiar"]


def registrar_huesped():
    while True:
        nombre = input("Nombre del huesped: ")
        if nombre.strip() != "":
            break
        print("El nombre no puede estar vacio.")
        
    #Validacion de la cedula 10 digitos y no letras
    while True:
        cedula = input("Cedula: ")
        if len(cedula) == 10 and cedula.isdigit():
            if cedula in [huesped.cedula for huesped in lista_huespedes]:
                print("La cedula ya esta registrada. Ingrese una cedula diferente.")
            else:
                break
        else:
            print("La cedula debe tener 10 digitos y ser numerica.")
    
    #Validacion del correo que contenga @ y .
    while True:
        correo = input("Correo: ")
        if "@" in correo and "." in correo:
            break
        print("Correo invalido.")
        
    #Creacion del huesped y agregarlo a la lista
    huesped_variable = Huesped(nombre, cedula, correo)
    lista_huespedes.append(huesped_variable)
    print("Huesped registrado con exito.\n")

#Buscar un huesped por su cedula
def buscar_huesped(cedula):
    for huesped in lista_huespedes:
        if huesped.cedula == cedula:
            return huesped
    return None

#Agregar una reserva a un huesped existente meduante su cedula
def agregar_reserva_huesped():
    cedula_busqueda = input("Ingrese la cedula del huesped: ")
    huesped = buscar_huesped(cedula_busqueda)
    if huesped:
        while True:
            print("Tipos de habitaciones: ")
            print("1.Individual\n2.Doble\n3.Suite\n4.Familiar")
            try:
                opcion = int(input("Ingrese el tipo de habtiacion: "))
                if 1 <= opcion <=4:
                    tipo_habitacion = tipos_de_habitaciones[opcion -1]
                    break
                else:
                    print("Opcion invalida. Eliga una opcion entre 1 a 4.")
            except ValueError:
                print("Opcion invalida.")
            
        #Validacion del formato de la fecha DD/MM/AAAA
        while True:
            fecha_entrada = input("Fecha de entrada (DD/MM/AAAA): ")
            if len(fecha_entrada) == 10 and fecha_entrada[2] == "/" and fecha_entrada[5] == "/":
                break
            print("Fecha invalida Foramto (DD/MM/AAAA).")
        while True:
            fecha_salida = input("Fecha de salida (DD/MM/AAAA): ")
            if len(fecha_salida) == 10 and fecha_salida[2] == "/" and fecha_salida[5] == "/":
                break
            print("Fecha invalida Foramto (DD/MM/AAAA).")
            
        #Creacion del diccionario de la reserva
        diccionario_reserva = {
            "fecha_entrada": fecha_entrada,
            "fecha_salida": fecha_salida,
            "habitacion": tipo_habitacion
        }
        #Enviamos el diccionario a la clase huesped para agregar la reserva
        huesped.agregar_reserva(diccionario_reserva)
        print("Reserva agregada con exito.")
    else:
        print("No se encontro el huesped con la cedula ingresada.")
    
def mostrar_reservas_huespedes():
    if lista_huespedes:
        for huesped in lista_huespedes:
            huesped.mostrar_reservas()
    else:
        print("No hay reservas registradas.")

def mostrar_huespedes_registrados():
    if lista_huespedes:
        for huesped in lista_huespedes:
            huesped.mostrar_todos_datos()
    else:
        print("No hay huespedes registrados.")     

            
    