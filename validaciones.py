from utilidades import (
    es_letra,
    calcular_longitud
)


def validar_contrasena_vacia(contrasena: str) -> bool:
    """
    Verifica si la contraseña está vacía.

    Args:
        contrasena (str): contraseña a validar.

    Returns:
        bool: True si es válida, False si está vacía.
    """

    if calcular_longitud(contrasena) == 0:
        return False

    return True


def validar_longitud_minima(contrasena: str) -> bool:
    """
    Verifica si la contraseña tiene
    al menos 8 caracteres.

    Args:
        contrasena (str): contraseña a validar.

    Returns:
        bool: True si cumple la longitud mínima.
    """

    if calcular_longitud(contrasena) >= 8:
        return True

    return False


def validar_primer_caracter(contrasena: str) -> bool:
    """
    Verifica que la contraseña
    no comience con espacio.

    Args:
        contrasena (str): contraseña a validar.

    Returns:
        bool: True si el primer carácter es válido.
    """

    if ord(contrasena[0]) == 32:
        return False

    return True


def validar_contiene_letra(contrasena: str) -> bool:
    """
    Verifica si la contraseña
    contiene al menos una letra.

    Args:
        contrasena (str): contraseña a validar.

    Returns:
        bool: True si contiene letras.
    """

    for caracter in contrasena:

        if es_letra(caracter):
            return True

    return False


def validar_contrasena(contrasena: str) -> bool:
    """
    Ejecuta todas las validaciones obligatorias
    de la contraseña.

    Validaciones:
    - no vacía
    - mínimo 8 caracteres
    - no comenzar con espacio
    - contener al menos una letra

    Args:
        contrasena (str): contraseña a validar.

    Returns:
        bool: True si la contraseña es válida.
    """

    if not validar_contrasena_vacia(contrasena):
        print("Error. La contraseña no puede estar vacía.")
        return False

    if not validar_longitud_minima(contrasena):
        print(
            "Error. La contraseña debe tener "
            "al menos 8 caracteres."
        )
        return False

    if not validar_primer_caracter(contrasena):
        print(
            "Error. La contraseña no puede "
            "comenzar con espacios."
        )
        return False

    if not validar_contiene_letra(contrasena):
        print(
            "Error. La contraseña debe "
            "contener al menos una letra."
        )
        return False

    return True


def pedir_contrasena() -> str:
    """
    Solicita una contraseña al usuario
    hasta que sea válida.

    Returns:
        str: contraseña válida.
    """

    contrasena = ""

    while True:

        contrasena = input(
            "\nIngrese una contraseña: "
        )

        if validar_contrasena(contrasena):
            break

    return contrasena