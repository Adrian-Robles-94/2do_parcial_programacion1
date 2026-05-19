from utilidades import es_letra, es_numero, es_simbolo, calcular_longitud


def validar_nivel_seguridad(contrasena: str) -> None:
    """
    Determina el nivel de seguridad de una contraseña.

    Niveles:
    - Débil
    - Media
    - Fuerte

    Args:
        contrasena (str): contraseña a analizar.
    """

    cantidad_letras = 0
    cantidad_numeros = 0
    cantidad_simbolos = 0

    longitud = calcular_longitud(contrasena)

    for caracter in contrasena:

        if es_letra(caracter):
            cantidad_letras += 1

        elif es_numero(caracter):
            cantidad_numeros += 1

        elif es_simbolo(caracter):
            cantidad_simbolos += 1

    if longitud >= 8 and longitud <= 9 and cantidad_letras == longitud:
        print("\nNivel de seguridad: DÉBIL")

    elif cantidad_letras > 0 and cantidad_numeros > 0 and cantidad_simbolos == 0:
        print("\nNivel de seguridad: MEDIA")

    elif (
        longitud >= 12
        and cantidad_letras > 0
        and cantidad_numeros > 0
        and cantidad_simbolos > 0
    ):
        print("\nNivel de seguridad: FUERTE")

    else:
        print("\nLa contraseña no cumple criterios suficientes.")


def buscar_caracter(contrasena: str, caracter_buscado: str) -> None:
    """
    Busca un carácter dentro de la contraseña
    mostrando cantidad de apariciones y posiciones.

    Args:
        contrasena (str): contraseña a analizar.
        caracter_buscado (str): carácter a buscar.
    """

    cantidad = 0
    posicion = 0

    print("\nPosiciones encontradas:")

    for caracter in contrasena:

        if caracter == caracter_buscado:
            print(posicion)
            cantidad += 1

        posicion += 1

    print(f"\nEl carácter '{caracter_buscado}' " f"aparece {cantidad} veces.")


def mostrar_contrasena_invertida(contrasena: str) -> None:
    """
    Muestra la contraseña invertida manualmente.

    No utiliza slicing.

    Args:
        contrasena (str): contraseña a invertir.
    """

    invertida = ""

    indice = calcular_longitud(contrasena) - 1

    while indice >= 0:

        invertida += contrasena[indice]

        indice -= 1

    print("\nContraseña invertida:")
    print(invertida)


def verificar_palindromo(contrasena: str) -> None:
    """
    Verifica si la contraseña es un palíndromo.

    Args:
        contrasena (str): contraseña a analizar.
    """

    izquierda = 0
    derecha = calcular_longitud(contrasena) - 1

    es_palindromo = True

    while izquierda < derecha:

        if contrasena[izquierda] != contrasena[derecha]:
            es_palindromo = False

        izquierda += 1
        derecha -= 1

    if es_palindromo:
        print("\nLa contraseña es un palíndromo.")

    else:
        print("\nLa contraseña NO es un palíndromo.")
