from utilidades import es_letra, es_numero, es_simbolo, es_espacio, calcular_longitud


def contar_tipos_caracteres(contrasena: str) -> None:
    """
    Cuenta la cantidad de letras, números,
    símbolos y espacios presentes en la contraseña.

    Args:
        contrasena (str): contraseña a analizar.
    """

    cantidad_letras = 0
    cantidad_numeros = 0
    cantidad_simbolos = 0
    cantidad_espacios = 0

    for caracter in contrasena:

        if es_letra(caracter):
            cantidad_letras += 1

        elif es_numero(caracter):
            cantidad_numeros += 1

        elif es_espacio(caracter):
            cantidad_espacios += 1

        elif es_simbolo(caracter):
            cantidad_simbolos += 1

    print("\n--- TIPOS DE CARACTERES ---")
    print(f"Letras: {cantidad_letras}")
    print(f"Números: {cantidad_numeros}")
    print(f"Símbolos: {cantidad_simbolos}")
    print(f"Espacios: {cantidad_espacios}")


def calcular_porcentaje(parte: int, total: int) -> float:
    """
    Calcula el porcentaje entre dos valores.

    Args:
        parte (int): valor parcial.
        total (int): valor total.

    Returns:
        float: porcentaje calculado.
    """

    if total == 0:
        return 0.0

    porcentaje = (parte * 100) / total

    return porcentaje


def contar_repetidos_consecutivos(contrasena: str) -> int:
    """
    Cuenta grupos de caracteres repetidos consecutivos.

    Ejemplo:
    aaBB22!!
    devuelve 4.

    Args:
        contrasena (str): contraseña a analizar.

    Returns:
        int: cantidad de repeticiones consecutivas.
    """

    repeticiones = 0
    longitud = calcular_longitud(contrasena)

    indice = 0

    while indice < longitud - 1:

        if contrasena[indice] == contrasena[indice + 1]:
            repeticiones += 1

        indice += 1

    return repeticiones


def generar_reporte_estadistico(contrasena: str) -> None:
    """
    Genera un reporte estadístico completo
    sobre la contraseña ingresada.

    Args:
        contrasena (str): contraseña a analizar.
    """

    letras = 0
    numeros = 0
    simbolos = 0
    espacios = 0

    for caracter in contrasena:

        if es_letra(caracter):
            letras += 1

        elif es_numero(caracter):
            numeros += 1

        elif es_espacio(caracter):
            espacios += 1

        elif es_simbolo(caracter):
            simbolos += 1

    longitud_total = calcular_longitud(contrasena)

    porcentaje_letras = calcular_porcentaje(letras, longitud_total)

    porcentaje_numeros = calcular_porcentaje(numeros, longitud_total)

    porcentaje_simbolos = calcular_porcentaje(simbolos, longitud_total)

    repetidos = contar_repetidos_consecutivos(contrasena)

    print("\n--- REPORTE ESTADÍSTICO ---")
    print(f"Longitud total: {longitud_total}")

    print(f"Porcentaje de letras: " f"{porcentaje_letras:.2f}%")

    print(f"Porcentaje de números: " f"{porcentaje_numeros:.2f}%")

    print(f"Porcentaje de símbolos: " f"{porcentaje_simbolos:.2f}%")

    print(f"Cantidad de caracteres repetidos consecutivos: " f"{repetidos}")
