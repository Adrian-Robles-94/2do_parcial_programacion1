import archivos
import alumnos
import estadisticas

def iniciar_programa():
    """
    Punto de entrada general del sistema. Carga los datos e inicia el bucle del menú interactivo.
    
    Args:
        Ninguno.
        
    Returns:
        None.
    """
    base_alumnos = archivos.cargar_datos()

    while True:
        print("\n=====================================")
        print("  SISTEMA DE GESTIÓN DE ALUMNOS UTN  ")
        print("=====================================")
        print("1. Registrar Alumno")
        print("2. Modificar Alumno")
        print("3. Eliminar Alumno")
        print("4. Buscar Alumno")
        print("5. Mostrar Alumnos")
        print("6. Calcular Estadísticas")
        print("7. Salir")
        print("=====================================")
        
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                alumnos.registrar_alumno(base_alumnos)
                # Auto-guardado después de agregar
                archivos.guardar_datos(base_alumnos) 
            case "2":
                alumnos.modificar_alumno(base_alumnos)
                # Auto-guardado después de modificar
                archivos.guardar_datos(base_alumnos) 
            case "3":
                alumnos.eliminar_alumno(base_alumnos)
                # Auto-guardado después de eliminar
                archivos.guardar_datos(base_alumnos) 
            case "4":
                alumnos.buscar_alumno(base_alumnos)
            case "5":
                alumnos.mostrar_alumnos(base_alumnos)
            case "6":
                estadisticas.calcular_estadisticas(base_alumnos)
            case "7":
                # Como ya se guarda solo, simplemente nos despedimos y rompemos el bucle
                print("Saliendo del sistema. ¡Éxitos en la cursada!")
                break
            case _:
                print("Opción inválida, intente de nuevo.")

# Ejecución única de la aplicación
iniciar_programa()