def validar_dni(mensaje):
    """
    Solicita el DNI asegurando que solo contenga números y tenga entre 7 y 8 dígitos.
    
    Args:
        mensaje (str): El texto informativo para pedir el DNI en la terminal.
        
    Returns:
        str: El DNI validado en formato texto (ideal para usar como clave de diccionario).
    """
    while True:
        dni = input(mensaje)
        
        if dni.isdigit() == True:
            if len(dni) >= 7 and len(dni) <= 8:
                return dni
            else:
                print("Error: El DNI debe tener entre 7 y 8 dígitos.")
        else:
            print("Error: Ingreso inválido. El DNI debe contener únicamente números.")

def validar_dni_duplicado(dni, alumnos):
    """
    Comprueba si un número de DNI ya está registrado como clave en el sistema.
    
    Args:
        dni (str): El documento de identidad que se quiere verificar.
        alumnos (dict): El diccionario que almacena los alumnos registrados.
        
    Returns:
        bool: True si el DNI ya existe, False en caso contrario.
    """
    if dni in alumnos:
        return True
    else:
        return False

def validar_edad(mensaje):
    """
    Solicita la edad controlando que sean solo números para evitar que el programa falle.
    
    Args:
        mensaje (str): El texto informativo en la terminal.
        
    Returns:
        int: Un número entero validado entre 1 y 120 años.
    """
    while True:
        entrada = input(mensaje)
        
        if entrada.isdigit() == True:
            edad = int(entrada)
            if edad >= 1 and edad <= 120:
                return edad
            else:
                print("Error: La edad debe estar entre 1 y 120 años.")
        else:
            print("Error: Ingresó letras o caracteres inválidos. Solo se permiten números enteros.")

def validar_nota(mensaje):
    """
    Solicita la nota verificando que sea un valor numérico válido (entero o con decimales).
    
    Args:
        mensaje (str): El texto informativo en la terminal.
        
    Returns:
        float: Un número decimal validado entre 0.0 y 10.0.
    """
    while True:
        entrada = input(mensaje)
        
        if entrada.replace(".", "", 1).isdigit() == True:
            nota = float(entrada)
            if nota >= 0.0 and nota <= 10.0:
                return nota
            else:
                print("Error: La nota debe ser un número entre 0 y 10.")
        else:
            print("Error: Ingreso inválido. Use solo números (y un punto para decimales).")

def validar_texto(mensaje):
    """
    Asegura que el ingreso sea únicamente de letras, sin números ni símbolos raros.
    
    Args:
        mensaje (str): El texto informativo para guiar al usuario.
        
    Returns:
        str: El texto validado (permite espacios entre nombres).
    """
    while True:
        texto = input(mensaje)
        
        if texto.replace(" ", "").isalpha() == True:
            return texto
        else:
            print("Error: El campo no puede estar vacío y debe contener únicamente letras.")