import validaciones
import archivos

def registrar_alumno(diccionario_alumnos: dict, ruta_archivo: str) -> None:
    """
    Gestiona el flujo interactivo para registrar un nuevo alumno.
    Valida cada campo utilizando el módulo de validaciones antes de insertarlo.
    Garantiza la unicidad del DNI y persiste los cambios inmediatamente en el JSON.
    """
    print("\n--- Registrar Nuevo Alumno ---")
    
    # 1. Captura y Validación de DNI
    while True:
        dni = input("Ingrese el DNI (solo números, entre 7 y 9 dígitos): ").strip()
        if not validaciones.validar_dni_formato(dni):
            print("Error: El formato del DNI es inválido.")
            continue
        if validaciones.validar_dni_duplicado(dni, diccionario_alumnos):
            print("Error: Ya existe un alumno registrado con ese DNI.")
            return  # Aborta la operación para evitar corrupción por duplicación
        break

    # 2. Captura y Validación de Nombre
    while True:
        nombre_raw = input("Ingrese el Nombre: ")
        nombre = validaciones.validar_texto_vacio(nombre_raw)
        if nombre is None:
            print("Error: El nombre no puede estar vacío.")
            continue
        break

    # 3. Captura y Validación de Apellido
    while True:
        apellido_raw = input("Ingrese el Apellido: ")
        apellido = validaciones.validar_texto_vacio(apellido_raw)
        if apellido is None:
            print("Error: El apellido no puede estar vacío.")
            continue
        break

    # 4. Captura y Validación de Edad
    while True:
        edad_raw = input("Ingrese la Edad: ")
        edad = validaciones.validar_edad(edad_raw)
        if edad is None:
            print("Error: La edad debe ser un número entero mayor o igual a 0.")
            continue
        break

    # 5. Captura y Validación de Nota
    while True:
        nota_raw = input("Ingrese la Nota (0 a 10): ")
        nota = validaciones.validar_nota(nota_raw)
        if nota is None:
            print("Error: La nota debe ser un número real entre 0 y 10.")
            continue
        break

    # Inserción en la estructura de datos (Clave: DNI -> Valor: Diccionario de datos)
    diccionario_alumnos[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }

    # Persistencia automática e inmediata
    if archivos.guardar_alumnos(ruta_archivo, diccionario_alumnos):
        print(f"\nÉxito: Alumno {nombre} {apellido} registrado y guardado correctamente.")


def listar_alumnos(diccionario_alumnos: dict) -> None:
    """
    Muestra en pantalla la totalidad de los alumnos registrados bajo un formato
    tabular limpio. Maneja de forma lógica el caso de un sistema sin registros.
    """
    print("\n--- Listado de Alumnos ---")
    if not diccionario_alumnos:
        print("No hay alumnos registrados en el sistema.")
        return

    # Diseño de la tabla con alineación estricta
    print(f"{'DNI':<12} | {'Apellido':<20} | {'Nombre':<20} | {'Edad':<5} | {'Nota':<5}")
    print("-" * 72)
    
    for dni, datos in diccionario_alumnos.items():
        print(f"{dni:<12} | {datos['apellido']:<20} | {datos['nombre']:<20} | {datos['edad']:<5} | {datos['nota']:<5.2f}")


def buscar_alumno(diccionario_alumnos: dict) -> None:
    """
    Realiza una búsqueda directa indexada por la clave primaria (DNI)
    ofreciendo una respuesta inmediata de O(1) en términos de eficiencia.
    """
    print("\n--- Buscar Alumno ---")
    dni = input("Ingrese el DNI del alumno a buscar: ").strip()
    
    if dni in diccionario_alumnos:
        datos = diccionario_alumnos[dni]
        print(f"\n[Registro Encontrado]")
        print(f"DNI: {dni}")
        print(f"Alumno: {datos['apellido']}, {datos['nombre']}")
        print(f"Edad: {datos['edad']} años")
        print(f"Nota: {datos['nota']}")
    else:
        print("Error: El alumno con el DNI provisto no se encuentra en el sistema.")


def modificar_alumno(diccionario_alumnos: dict, ruta_archivo: str) -> None:
    """
    Permite la actualización selectiva de los campos de un alumno existente.
    Si el usuario presiona ENTER, conserva el valor original del campo.
    Cualquier modificación pasa obligatoriamente por el filtro de validaciones.
    """
    print("\n--- Modificar Alumno ---")
    dni = input("Ingrese el DNI del alumno a modificar: ").strip()

    if dni not in diccionario_alumnos:
        print("Error: El alumno con el DNI provisto no existe en el sistema.")
        return

    datos_actuales = diccionario_alumnos[dni]
    print(f"\nModificando registro de: {datos_actuales['apellido']}, {datos_actuales['nombre']}")
    print("(Presione ENTER para mantener el valor actual de un campo)")

    # Modificación de Nombre
    nombre_raw = input(f"Nombre [{datos_actuales['nombre']}]: ")
    if nombre_raw.strip() != "":
        nombre_valido = validaciones.validar_texto_vacio(nombre_raw)
        if nombre_valido:
            datos_actuales['nombre'] = nombre_valido
        else:
            print("Omitido: Formato de nombre inválido. No se aplicaron cambios en este campo.")

    # Modificación de Apellido
    apellido_raw = input(f"Apellido [{datos_actuales['apellido']}]: ")
    if apellido_raw.strip() != "":
        apellido_valido = validaciones.validar_texto_vacio(apellido_raw)
        if apellido_valido:
            datos_actuales['apellido'] = apellido_valido
        else:
            print("Omitido: Formato de apellido inválido. No se aplicaron cambios en este campo.")

    # Modificación de Edad con bucle de reintento si el formato ingresado es erróneo
    while True:
        edad_raw = input(f"Edad [{datos_actuales['edad']}]: ")
        if edad_raw.strip() == "":
            break  # Conserva el valor actual
        edad_valido = validaciones.validar_edad(edad_raw)
        if edad_valido is not None:
            datos_actuales['edad'] = edad_valido
            break
        print("Error: Edad inválida. Debe ser un número entero mayor o igual a 0.")

    # Modificación de Nota con bucle de reintento si la métrica está fuera de rango
    while True:
        nota_raw = input(f"Nota [{datos_actuales['nota']}]: ")
        if nota_raw.strip() == "":
            break  # Conserva el valor actual
        nota_valido = validaciones.validar_nota(nota_raw)
        if nota_valido is not None:
            datos_actuales['nota'] = nota_valido
            break
        print("Error: Nota inválida. Debe ser un número real entre 0 y 10.")

    # Persistencia automatizada tras procesar los cambios con éxito
    if archivos.guardar_alumnos(ruta_archivo, diccionario_alumnos):
        print("\nÉxito: Los datos del alumno fueron actualizados y guardados en el archivo JSON.")


def eliminar_alumno(diccionario_alumnos: dict, ruta_archivo: str) -> None:
    """
    Remueve una entrada del diccionario principal basándose en el DNI.
    Requiere confirmación explícita del operador y sincroniza inmediatamente con el JSON.
    """
    print("\n--- Eliminar Alumno ---")
    dni = input("Ingrese el DNI del alumno a eliminar: ").strip()

    if dni not in diccionario_alumnos:
        print("Error: El alumno con el DNI provisto no existe en el sistema.")
        return

    datos = diccionario_alumnos[dni]
    confirmacion = input(f"¿Confirmar la eliminación permanente de {datos['apellido']}, {datos['nombre']}? (S/N): ").strip().upper()

    if confirmacion == "S":
        del diccionario_alumnos[dni]
        if archivos.guardar_alumnos(ruta_archivo, diccionario_alumnos):
            print("Éxito: El alumno fue eliminado por completo del sistema.")
    else:
        print("Operación cancelada. Registro intacto.")