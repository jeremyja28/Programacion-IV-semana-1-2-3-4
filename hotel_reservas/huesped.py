class Huesped:
    def __init__(self, nombre, cedula, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.reservas = []
        
    # Metodo para agregar una nueva reserva al huesped
    def agregar_reserva(self, datos_reserva):
        self.reservas.append(datos_reserva)
    
    # Metodo para las reservas de un huesped
    def mostrar_reservas(self):
        if self.reservas:
            print(f"Reservas de {self.nombre} con cedula {self.cedula}:")
            for i, reserva in enumerate(self.reservas, 1):
                print(f"  Reserva #{i}:")
                print(f"    Fecha de entrada: {reserva['fecha_entrada']}")
                print(f"    Fecha de salida: {reserva['fecha_salida']}")
                print(f"    Habitación: {reserva['habitacion']}")
            
    
    #Metodo para imprimir todos los datos de los huespedes
                
    def mostrar_todos_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cedula: {self.cedula}")
        print(f"Correo: {self.correo}")
        
        