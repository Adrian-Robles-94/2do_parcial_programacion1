import validaciones
import archivos

def registrar_alumno(diccionario_alumnos: dict, ruta_archivo: str) -> None:
    print("\n--- Registrar Alumno ---")
    while True:
        dni = input("Ingrese el DNI: ").strip()
        if not validaciones.validar_dni_formato(dni):
            print("Error: Formato de DNI inválido.")
            continue
        if validaciones.validar_dni_duplicado(dni, diccionario_alumnos):
            print("Error: El DNI ya se encuentra registrado.")
            return
        break

    while True:
        nombre_raw = input("Ingrese el Nombre: ")
        nombre = validaciones.validar_texto_vacio(nombre_raw)
        if nombre is None:
            print("Error: Nombre inválido.")
            continue
        break

    while True:
        apellido_raw = input("Ingrese el Apellido: ")
        apellido = validaciones.validar_texto_vacio(apellido_raw)
        if apellido is None:
            print("Error: Apellido inválido.")
            continue
        break

    while True:
        edad_raw = input("Ingrese la Edad: ")
        edad = validaciones.validar_edad(edad_raw)
        if edad is None:
            print("Error: La edad no puede ser negativa ni superar los 120 años.")
            continue
        break

    while True:
        nota_raw = input("Ingrese la Nota (0-10): ")
        nota = validaciones.validar_nota(nota_raw)
        if nota is None:
            print("Error: La nota debe estar entre 0 y 10.")
            continue
        break

    diccionario_alumnos[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }

    if archivos.guardar_alumnos(ruta_archivo, diccionario_alumnos):
        print("Alumno registrado con éxito.")

def listar_alumnos(diccionario_alumnos: dict) -> None:
    print("\n--- Listado de Alumnos ---")
    if not diccionario_alumnos:
        print("No hay alumnos registrados.")
        return
    
    # Formato vertical sugerido de manera exacta por la consigna
    for dni, datos in diccionario_alumnos.items():
        print(f"DNI: {dni}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Apellido: {datos['apellido']}")
        print(f"Edad: {datos['edad']}")
        print(f"Nota: {datos['nota']}")
        print("-" * 30)

def buscar_alumno(diccionario_alumnos: dict) -> None:
    print("\n--- Buscar Alumno ---")
    dni = input("Ingrese el DNI a buscar: ").strip()
    if dni in diccionario_alumnos:
        datos = diccionario_alumnos[dni]
        print(f"\nAlumno Encontrado:")
        print(f"DNI: {dni}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Apellido: {datos['apellido']}")
        print(f"Edad: {datos['edad']}")
        print(f"Nota: {datos['nota']}")
    else:
        print("Error: Alumno no encontrado.")

def modificar_alumno(diccionario_alumnos: dict, ruta_archivo: str) -> None:
    print("\n--- Modificar Alumno ---")
    dni = input("Ingrese el DNI del alumno a modificar: ").strip()
    if dni not in diccionario_alumnos:
        print("Error: El alumno no existe.")
        return

    datos_actuales = diccionario_alumnos[dni]
    print("(Presione ENTER para mantener el valor actual)")

    while True:
        nombre_raw = input(f"Nombre [{datos_actuales['nombre']}]: ")
        if nombre_raw.strip() == "": break
        valido = validaciones.validar_texto_vacio(nombre_raw)
        if valido: datos_actuales['nombre'] = valido; break
        print("Error: Nombre inválido.")

    while True:
        apellido_raw = input(f"Apellido [{datos_actuales['apellido']}]: ")
        if apellido_raw.strip() == "": break
        valido = validaciones.validar_texto_vacio(apellido_raw)
        if valido: datos_actuales['apellido'] = valido; break
        print("Error: Apellido inválido.")

    while True:
        edad_raw = input(f"Edad [{datos_actuales['edad']}]: ")
        if edad_raw.strip() == "": break
        valido = validaciones.validar_edad(edad_raw)
        if valido is not None: datos_actuales['edad'] = valido; break
        print("Error: Edad inválida.")

    while True:
        nota_raw = input(f"Nota [{datos_actuales['nota']}]: ")
        if nota_raw.strip() == "": break
        valido = validaciones.validar_nota(nota_raw)
        if valido is not None: datos_actuales['nota'] = valido; break
        print("Error: Nota inválida.")

    if archivos.guardar_alumnos(ruta_archivo, diccionario_alumnos):
        print("Datos modificados correctamente.")

def eliminar_alumno(diccionario_alumnos: dict, ruta_archivo: str) -> None:
    print("\n--- Eliminar Alumno ---")
    dni = input("Ingrese el DNI del alumno a eliminar: ").strip()
    if dni in diccionario_alumnos:
        confirmar = input(f"¿Seguro que desea eliminar a {diccionario_alumnos[dni]['nombre']}? (S/N): ").strip().upper()
        if confirmar == "S":
            del diccionario_alumnos[dni]
            if archivos.guardar_alumnos(ruta_archivo, diccionario_alumnos):
                print("Alumno eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Error: El DNI no existe.")