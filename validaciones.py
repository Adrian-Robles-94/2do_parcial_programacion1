def validar_dni_formato(dni_str: str) -> bool:
    """
    Verifica que la cadena ingresada contenga únicamente dígitos numéricos
    y cumpla con una longitud razonable para un DNI.
    """
    dni_limpio = dni_str.strip()
    return dni_limpio.isdigit() and len(dni_limpio) >= 7 and len(dni_limpio) <= 9

def validar_dni_duplicado(dni: str, diccionario_alumnos: dict) -> bool:
    """
    Comprueba si el DNI ya se encuentra registrado como clave principal 
    dentro del diccionario de alumnos del sistema.
    """
    return dni in diccionario_alumnos

def validar_edad(edad_str: str) -> int | None:
    """
    Valida que la edad ingresada sea un número entero, que no sea negativa
    y que se encuentre dentro de un límite biológico lógico (máximo 120 años).
    Si es válida, devuelve el entero. Si no, devuelve None.
    """
    edad_limpia = edad_str.strip()
    if not edad_limpia.isdigit():
        return None
    
    edad_num = int(edad_limpia)
    # Condición métrica estricta: entre 0 y 120 años
    if edad_num < 0 or edad_num > 120:
        return None
        
    return edad_num

def validar_nota(nota_str: str) -> float | None:
    """
    Valida que la nota ingresada corresponda a un valor numérico real (float)
    y que se encuentre estrictamente dentro del rango académico de 0 a 10.
    Si es válida, devuelve el float. Si no, devuelve None.
    """
    nota_limpia = nota_str.strip().replace(",", ".")
    
    try:
        nota_num = float(nota_limpia)
        if nota_num >= 0.0 and nota_num <= 10.0:
            return nota_num
        return None
    except ValueError:
        return None

def validar_texto_vacio(texto_str: str) -> str | None:
    """
    Asegura que campos alfabéticos críticos (Nombre, Apellido) no queden
    vacíos y contengan únicamente caracteres alfabéticos (letras y espacios).
    Bloquea números o símbolos especiales.
    """
    texto_limpio = texto_str.strip()
    if len(texto_limpio) == 0:
        return None
    
    # Reemplazamos los espacios para validar puramente caracteres alfabéticos
    # Esto permite nombres compuestos como "Juan Carlos" pero rechaza "Juan123"
    if not texto_limpio.replace(" ", "").isalpha():
        return None
        
    return texto_limpio.title()