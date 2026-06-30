def calcular_estadisticas(alumnos):
    """
    Recorre los datos en memoria para procesar, computar y mostrar las métricas de la cursada,
    incluyendo los porcentajes y el formato detallado del mejor promedio.
    
    Args:
        alumnos (dict): El diccionario principal con los datos de los estudiantes.
        
    Returns:
        None. Muestra los resultados directamente impresos en la consola.
    """
    if alumnos == {}:
        print("No hay alumnos registrados para calcular estadísticas.")
    else:
        total_alumnos = 0
        suma_notas = 0.0
        aprobados = 0
        desaprobados = 0
        
        # Variables para rastrear al mejor alumno
        nota_mas_alta = -1.0
        mejor_nombre = ""
        mejor_apellido = ""
        mejor_dni = ""

        for dni, datos in alumnos.items():
            total_alumnos = total_alumnos + 1
            suma_notas = suma_notas + datos["nota"]

            if datos["nota"] >= 6.0:
                aprobados = aprobados + 1
            else:
                desaprobados = desaprobados + 1

            # Si encontramos una nota mayor, actualizamos todos los datos
            if datos["nota"] > nota_mas_alta:
                nota_mas_alta = datos["nota"]
                mejor_nombre = datos["nombre"]
                mejor_apellido = datos["apellido"]
                mejor_dni = dni

        promedio = suma_notas / total_alumnos
        porcentaje_aprobados = (aprobados * 100) / total_alumnos
        porcentaje_desaprobados = (desaprobados * 100) / total_alumnos

        print("\n--- REPORTES DE LA CURSADA ---")
        print(f"Total de alumnos: {total_alumnos}")
        print(f"Promedio general: {promedio:.2f}")
        print(f"Alumnos aprobados: {aprobados} ({porcentaje_aprobados:.2f}%)")
        print(f"Alumnos desaprobados: {desaprobados} ({porcentaje_desaprobados:.2f}%)")
        print("\n--- MEJOR ALUMNO ---")
        print(f"{mejor_apellido}, {mejor_nombre}")
        print(f"DNI: {mejor_dni}")
        print(f"NOTA: {nota_mas_alta}")