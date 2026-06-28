import archivos
import alumnos
import estadisticas

# Definición de la ruta del archivo de persistencia como constante global
RUTA_BASE_DATOS = "alumnos.json"

def mostrar_menu() -> None:
    """
    Imprime en la consola la interfaz visual del menú interactivo.
    Mantiene un diseño limpio y profesional para el operador.
    """
    print("\n========================================")
    print("      SISTEMA DE GESTIÓN DE ALUMNOS     ")
    print("========================================")
    print("1. Registrar Alumno (Alta)")
    print("2. Listar Alumnos")
    print("3. Buscar Alumno por DNI")
    print("4. Modificar Alumno (Actualización)")
    print("5. Eliminar Alumno (Baja)")
    print("6. Mostrar Informe Estadístico")
    print("7. Salir del Sistema")
    print("========================================")


def ejecutar_aplicacion() -> None:
    """
    Función principal que controla el ciclo de vida de la aplicación.
    Orquesta la carga inicial de datos y el bucle de interacción.
    """
    # Carga inicial automatizada de datos desde el archivo JSON
    diccionario_alumnos = archivos.cargar_alumnos(RUTA_BASE_DATOS)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        # Estructura de control selectiva para derivar la lógica
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
            estadisticas.mostrar_informe_estadistico(diccionario_alumnos)
        elif opcion == "7":
            print("\nFinalizando ejecución. Sincronización con el almacenamiento exitosa. ¡Hasta luego!")
            break
        else:
            # Control analítico de errores: previene que opciones inválidas rompan el flujo
            print("Error: Opción inválida. Por favor, ingrese un número entero del 1 al 7.")


# Punto de entrada exclusivo del programa
if __name__ == "__main__":
    ejecutar_aplicacion()