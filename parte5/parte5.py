# Clase para representar una actividad o clase
class Actividad:
    def _init_(self, nombre, dia, hora_inicio, hora_fin):
        self.nombre = nombre
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

# Funcion para verificar si hay conflictos de horario
def verificar_conflicto(nueva_actividad, actividades):
    for actividad in actividades:
        if nueva_actividad.dia == actividad.dia:
            if (nueva_actividad.hora_inicio < actividad.hora_fin and nueva_actividad.hora_fin > actividad.hora_inicio):
                return True  # Hay un conflicto
    return False

# Funcion para registrar una actividad
def registrar_actividad():
    nombre = input("Ingrese el nombre de la clase o actividad: ")
    dia = input("Ingrese el dia de la semana (Lunes, Martes, etc.): ")
    hora_inicio = int(input("Ingrese la hora de inicio (en formato 24 horas, ej. 14 para las 2 PM): "))
    hora_fin = int(input("Ingrese la hora de fin (en formato 24 horas, ej. 16 para las 4 PM): "))

    return Actividad(nombre, dia, hora_inicio, hora_fin)

# Funcion principal para gestionar el horario
def gestionar_horario():
    actividades = []
    while True:
        print("\n1. Registrar nueva actividad")
        print("2. Mostrar horario")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nueva_actividad = registrar_actividad()
            if verificar_conflicto(nueva_actividad, actividades):
                print("Conflicto de horario! No se puede agregar esta actividad.")
            else:
                actividades.append(nueva_actividad)
                print(f"Actividad '{nueva_actividad.nombre}' agregada con exito.")
        
        elif opcion == "2":
            if not actividades:
                print("No hay actividades registradas.")
            else:
                print("\n--- Horario ---")
                for actividad in actividades:
                    print(f"{actividad.nombre} - {actividad.dia}, {actividad.hora_inicio}:00 a {actividad.hora_fin}:00")
        
        elif opcion == "3":
            break
        
        else:
            print("Opcion no valida, intente nuevamente.")

# Ejecutar el programa
gestionar_horario()