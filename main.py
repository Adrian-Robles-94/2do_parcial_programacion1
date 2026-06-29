import archivos
import alumnos
import estadisticas

RUTA_BASE_DATOS = "alumnos.json"

def mostrar_menu() -> None:
    # Ajustado rigurosamente al diseño del enunciado original
    print("\n======== GESTIÓN DE ALUMNOS ========")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadísticas")
    print("7. Salir")

def ejecutar_aplicacion() -> None:
    diccionario_alumnos = archivos.cargar_alumnos(RUTA_BASE_DATOS)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            alumnos.registrar_alumno(diccionario_alumnos, RUTA_BASE_DATOS)
        elif opcion == "2":
            alumnos.listar_alumnos(diccionario_alumnos)
        elif opcion == "3":
            alumnos.buscar_alumno(diccionario_alumnos)
        elif opcion == "4":
            alumnos.modificar_alumno(diccionario_alumnos, RUTA_BASE_DATOS)
        elif opcion == "5":
            alumnos.eliminar_alumno(diccionario_alumnos, RUTA_BASE_DATOS)
        elif opcion == "6":
            estadisticas.ver_estadisticas(diccionario_alumnos)
        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break
        else:
            print("Error: Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_aplicacion()