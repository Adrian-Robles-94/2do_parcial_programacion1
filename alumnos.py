import validaciones

def registrar_alumno(alumnos):
    """
    Pide los datos de un estudiante, los valida y los inserta en el diccionario principal.
    
    Args:
        alumnos (dict): El diccionario principal donde se agregará el nuevo registro.
        
    Returns:
        None. Modifica el diccionario recibido por parámetro.
    """
    print("\n--- REGISTRAR NUEVO ALUMNO ---")
    dni = validaciones.validar_dni("Ingrese el DNI del alumno: ")
    
    if validaciones.validar_dni_duplicado(dni, alumnos) == True:
        print("Error: Ya existe un alumno con ese DNI.")
    else:
        nombre = validaciones.validar_texto("Ingrese el Nombre: ")
        apellido = validaciones.validar_texto("Ingrese el Apellido: ")
        edad = validaciones.validar_edad("Ingrese la Edad: ")
        nota = validaciones.validar_nota("Ingrese la Nota Final: ")

        alumno_nuevo = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "nota": nota
        }
        
        alumnos[dni] = alumno_nuevo
        print("Alumno registrado con éxito en la memoria.")

def modificar_alumno(alumnos):
    """
    Busca un estudiante por DNI y permite actualizar de forma individual sus campos
    (nombre, apellido, edad y nota). Si el campo se deja vacío, no se modifica.
    
    Args:
        alumnos (dict): El diccionario principal donde se encuentra el estudiante.
        
    Returns:
        None.
    """
    print("\n--- MODIFICAR ALUMNO ---")
    dni = validaciones.validar_dni("Ingrese el DNI del alumno a modificar: ")

    if dni in alumnos:
        print("Deje el espacio en blanco (presione Enter) si no desea modificar el campo.")
        
        # --- Modificar Nombre ---
        while True:
            nombre = input("Nuevo Nombre: ")
            if nombre == "":
                break
            elif nombre.replace(" ", "").isalpha() == True:
                alumnos[dni]["nombre"] = nombre
                break
            else:
                print("Error: El nombre debe contener únicamente letras.")

        # --- Modificar Apellido ---
        while True:
            apellido = input("Nuevo Apellido: ")
            if apellido == "":
                break
            elif apellido.replace(" ", "").isalpha() == True:
                alumnos[dni]["apellido"] = apellido
                break
            else:
                print("Error: El apellido debe contener únicamente letras.")

        # --- Modificar Edad ---
        while True:
            edad_str = input("Nueva Edad: ")
            if edad_str == "":
                break
            elif edad_str.isdigit() == True:
                edad = int(edad_str)
                if edad >= 1 and edad <= 120:
                    alumnos[dni]["edad"] = edad
                    break
                else:
                    print("Error: La edad debe estar entre 1 y 120 años.")
            else:
                print("Error: Ingreso inválido. Use solo números enteros.")

        # --- Modificar Nota ---
        while True:
            nota_str = input("Nueva Nota: ")
            if nota_str == "":
                break
            elif nota_str.replace(".", "", 1).isdigit() == True:
                nota = float(nota_str)
                if nota >= 0.0 and nota <= 10.0:
                    alumnos[dni]["nota"] = nota
                    break
                else:
                    print("Error: La nota debe ser un número entre 0 y 10.")
            else:
                print("Error: Ingreso inválido. Use solo números (y un punto para decimales).")

        print("Modificación realizada con éxito.")
    else:
        print("El DNI no se encuentra registrado en el sistema.")

def eliminar_alumno(alumnos):
    """
    Remueve de forma permanente un registro de alumno usando su DNI como clave de búsqueda.
    
    Args:
        alumnos (dict): El diccionario principal de donde se eliminará el registro.
        
    Returns:
        None.
    """
    print("\n--- ELIMINAR ALUMNO ---")
    dni = validaciones.validar_dni("Ingrese el DNI del alumno a dar de baja: ")

    if dni in alumnos:
        del alumnos[dni]
        print("Alumno eliminado correctamente.")
    else:
        print("No se encontró ningún alumno con ese DNI.")

def buscar_alumno(alumnos):
    """
    Busca un alumno específico por su DNI y muestra sus datos si lo encuentra.
    
    Args:
        alumnos (dict): El diccionario principal donde se realiza la búsqueda.
        
    Returns:
        None.
    """
    print("\n--- BUSCAR ALUMNO ---")
    dni = validaciones.validar_dni("Ingrese el DNI del alumno a buscar: ")

    if dni in alumnos:
        datos = alumnos[dni]
        print(f"DNI: {dni} | {datos['apellido']}, {datos['nombre']} | Edad: {datos['edad']} | Nota: {datos['nota']}")
    else:
        print("No se encontró ningún alumno con ese DNI.")

def mostrar_alumnos(alumnos):
    """
    Itera sobre el diccionario para listar a todos los alumnos con un formato legible.
    
    Args:
        alumnos (dict): El diccionario principal que contiene los datos.
        
    Returns:
        None.
    """
    print("\n--- LISTADO DE ALUMNOS ---")
    if alumnos == {}:
        print("La base de datos está vacía.")
    else:
        for dni, datos in alumnos.items():
            print(f"DNI: {dni} | {datos['apellido']}, {datos['nombre']} | Edad: {datos['edad']} | Nota: {datos['nota']}")