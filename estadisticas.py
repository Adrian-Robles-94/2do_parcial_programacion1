def calcular_promedio_notas(diccionario_alumnos: dict) -> float:
    """
    Calcula la media aritmética de las notas de todos los alumnos registrados.
    Si el diccionario está vacío, retorna 0.0 para evitar divisiones por cero.
    """
    if not diccionario_alumnos:
        return 0.0
        
    total_notas = 0.0
    for datos in diccionario_alumnos.values():
        total_notas += datos["nota"]
        
    return total_notas / len(diccionario_alumnos)


def obtener_alumno_nota_maxima(diccionario_alumnos: dict) -> tuple | None:
    """
    Analiza los registros para identificar la nota más alta.
    Retorna una tupla con (DNI, diccionario_datos) del alumno con mejor desempeño.
    Si hay empate, devuelve el primero encontrado. Si está vacío, retorna None.
    """
    if not diccionario_alumnos:
        return None

    mejor_dni = None
    mejor_nota = -1.0 # Inicialización por debajo del límite mínimo válido

    for dni, datos in diccionario_alumnos.items():
        if datos["nota"] > mejor_nota:
            mejor_nota = datos["nota"]
            mejor_dni = dni

    return mejor_dni, diccionario_alumnos[mejor_dni]


def calcular_distribucion_academica(diccionario_alumnos: dict) -> dict:
    """
    Clasifica y cuenta cuantitativamente a los alumnos según criterios académicos estándar:
    - Promocionados (Aprobación Directa): Nota >= 7.0
    - Regulares (Aprobación No Directa): 4.0 <= Nota < 7.0
    - Libres / Reprobados: Nota < 4.0
    """
    distribucion = {
        "promocionados": 0,
        "regulares": 0,
        "libres": 0
    }

    for datos in diccionario_alumnos.values():
        nota = datos["nota"]
        if nota >= 7.0:
            distribucion["promocionados"] += 1
        elif nota >= 4.0:
            distribucion["regulares"] += 1
        else:
            distribucion["libres"] += 1

    return distribucion


def calcular_promedio_edad(diccionario_alumnos: dict) -> float:
    """
    Calcula la edad promedio del grupo estudiantil registrado.
    Maneja el caso de diccionario vacío retornando 0.0.
    """
    if not diccionario_alumnos:
        return 0.0

    total_edad = 0
    for datos in diccionario_alumnos.values():
        total_edad += datos["edad"]

    return total_edad / len(diccionario_alumnos)


def mostrar_informe_estadistico(diccionario_alumnos: dict) -> None:
    """
    Orquesta las funciones de cálculo de este módulo para presentar en pantalla
    un informe estadístico consolidado, claro y limpio.
    """
    print("\n--- Informe Estadístico del Sistema ---")
    if not diccionario_alumnos:
        print("No hay datos suficientes en el sistema para generar estadísticas.")
        return

    total_alumnos = len(diccionario_alumnos)
    promedio_notas = calcular_promedio_notas(diccionario_alumnos)
    promedio_edad = calcular_promedio_edad(diccionario_alumnos)
    distribucion = calcular_distribucion_academica(diccionario_alumnos)
    mejor_registro = obtener_alumno_nota_maxima(diccionario_alumnos)

    # Impresión métrica
    print(f"Total de alumnos evaluados: {total_alumnos}")
    print(f"Promedio general de notas:  {promedio_notas:.2f}")
    print(f"Promedio de edad del grupo: {promedio_edad:.1f} años")
    
    print("\n[Distribución de Estados Académicos]")
    print(f" -> Alumnos Promocionados (>= 7):  {distribucion['promocionados']} ({(distribucion['promocionados']/total_alumnos)*100:.1f}%)")
    print(f" -> Alumnos Regulares (4 a 6.9):   {distribucion['regulares']} ({(distribucion['regulares']/total_alumnos)*100:.1f}%)")
    print(f" -> Alumnos Libres / Reprobados (< 4): {distribucion['libres']} ({(distribucion['libres']/total_alumnos)*100:.1f}%)")

    if mejor_registro:
        dni, datos = mejor_registro
        print("\n[Rendimiento Destacado]")
        print(f" -> Alumno con Mayor Nota: {datos['apellido']}, {datos['nombre']} (DNI: {dni})")
        print(f" -> Calificación Obtenida: {datos['nota']:.2f}")