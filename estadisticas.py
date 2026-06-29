def ver_estadisticas(diccionario_alumnos: dict) -> None:
    print("\n======== ESTADÍSTICAS ========")
    total = len(diccionario_alumnos)
    print(f"Cantidad total de alumnos: {total}") # Requisito obligatorio 6.1
    
    if total == 0:
        print("Promedio de notas: 0.0")
        print("Alumno con mayor nota: N/A")
        print("Cantidad de aprobados (≥ 6): 0")
        print("Cantidad de desaprobados (< 6): 0")
        return

    suma_notas = 0
    aprobados = 0
    desaprobados = 0
    
    # Inicialización de variables para buscar el máximo
    dni_mayor_nota = None
    mayor_nota = -1.0

    for dni, datos in diccionario_alumnos.items():
        nota = datos["nota"]
        suma_notas += nota
        
        # Clasificación estricta según nota de aprobación de la consigna
        if nota >= 6.0:
            aprobados += 1
        else:
            desaprobados += 1
            
        # Búsqueda del alumno sobresaliente
        if nota > mayor_nota:
            mayor_nota = nota
            dni_mayor_nota = dni

    promedio = suma_notas / total
    print(f"Promedio de notas: {promedio:.2f}") # Requisito obligatorio 6.2
    
    # Información del alumno con mayor nota
    if dni_mayor_nota:
        al_max = diccionario_alumnos[dni_mayor_nota]
        print(f"Alumno con mayor nota: {al_max['apellido']}, {al_max['nombre']} (Nota: {mayor_nota})") # Requisito obligatorio 6.3
    
    print(f"Cantidad de aprobados (≥ 6): {aprobados}") # Requisito obligatorio 6.4
    print(f"Cantidad de desaprobados (< 6): {desaprobados}") # Requisito obligatorio 6.5