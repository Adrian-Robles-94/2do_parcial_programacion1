def mostrar_menu() -> None:
    """
    Muestra el menú principal del programa.
    """

    print("\n--- SISTEMA DE PROCESAMIENTO DE CONTRASEÑAS ---")
    print("1. Ingresar contraseña")
    print("2. Validar nivel de seguridad")
    print("3. Contar tipos de caracteres")
    print("4. Buscar carácter específico")
    print("5. Mostrar contraseña invertida")
    print("6. Generar reporte estadístico")
    print("7. Verificar si es palíndromo")
    print("8. Ordenar caracteres de la contraseña")
    print("9. Salir")


def pedir_opcion_menu() -> int:
    """
    Solicita una opción válida del menú.
    Solo permite números enteros entre 1 y 9.

    Returns:
        int: opción elegida por el usuario.
    """

    opcion = 0

    while opcion < 1 or opcion > 9:
        opcion = int(input("\nIngrese una opción (1-9): "))

        if opcion < 1 or opcion > 9:
            print("Error. Debe ingresar un número entre 1 y 9.")

    return opcion


def calcular_longitud(texto: str) -> int:
    """
    Calcula manualmente la longitud de una cadena.

    Args:
        texto (str): cadena a analizar.

    Returns:
        int: cantidad de caracteres.
    """

    contador = 0

    for _ in texto:
        contador += 1

    return contador


def es_letra(caracter: str) -> bool:
    """
    Determina si un carácter es una letra utilizando ASCII.

    Args:
        caracter (str): carácter a evaluar.

    Returns:
        bool: True si es letra, False en caso contrario.
    """

    codigo = ord(caracter)

    if codigo >= 65 and codigo <= 90:
        return True

    if codigo >= 97 and codigo <= 122:
        return True

    return False


def es_numero(caracter: str) -> bool:
    """
    Determina si un carácter es numérico utilizando ASCII.

    Args:
        caracter (str): carácter a evaluar.

    Returns:
        bool: True si es número, False en caso contrario.
    """

    codigo = ord(caracter)

    if codigo >= 48 and codigo <= 57:
        return True

    return False


def es_espacio(caracter: str) -> bool:
    """
    Determina si un carácter es un espacio.

    Args:
        caracter (str): carácter a evaluar.

    Returns:
        bool: True si es espacio, False en caso contrario.
    """

    if ord(caracter) == 32:
        return True

    return False


def es_simbolo(caracter: str) -> bool:
    """
    Determina si un carácter es uno de los símbolos permitidos.

    Símbolos válidos:
    ! " # $ % & ' ( ) * + , - . /

    Args:
        caracter (str): carácter a evaluar.

    Returns:
        bool: True si es símbolo válido, False en caso contrario.
    """

    codigo = ord(caracter)

    if codigo >= 33 and codigo <= 47:
        return True

    return False


def convertir_minuscula(caracter: str) -> str:
    """
    Convierte manualmente una letra mayúscula a minúscula.

    Args:
        caracter (str): carácter a convertir.

    Returns:
        str: carácter convertido.
    """

    codigo = ord(caracter)

    if codigo >= 65 and codigo <= 90:
        codigo += 32

    return chr(codigo)


def convertir_mayuscula(caracter: str) -> str:
    """
    Convierte manualmente una letra minúscula a mayúscula.

    Args:
        caracter (str): carácter a convertir.

    Returns:
        str: carácter convertido.
    """

    codigo = ord(caracter)

    if codigo >= 97 and codigo <= 122:
        codigo -= 32

    return chr(codigo)


def copiar_cadena(texto: str) -> str:
    """
    Realiza una copia manual de una cadena.

    Args:
        texto (str): cadena original.

    Returns:
        str: copia de la cadena.
    """

    copia = ""

    for caracter in texto:
        copia += caracter

    return copia