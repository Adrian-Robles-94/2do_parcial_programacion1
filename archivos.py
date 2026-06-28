import json

def cargar_alumnos(ruta_archivo: str) -> dict:
    """
    Lee el archivo JSON especificado y devuelve la información en un diccionario.
    Si el archivo no existe o está corrupto, maneja la excepción devolviendo
    un diccionario vacío para iniciar el sistema sin errores.
    """
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo: # Modo 'r' para lectura limpia y with para cierre seguro
            datos = json.load(archivo)
            return datos
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o su estructura está rota, retornamos un diccionario vacío
        # Esto cumple con el requerimiento de manejar la ausencia del archivo
        return {}

def guardar_alumnos(ruta_archivo: str, diccionario_alumnos: dict) -> bool:
    """
    Recibe el diccionario de alumnos y lo escribe de forma estructurada en el archivo JSON.
    Devuelve True si la operación fue exitosa, o False en caso contrario.
    """
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo: # Modo 'w' para sobreescritura controlada
            # Guardamos con indentación para mantener el archivo legible
            json.dump(diccionario_alumnos, archivo, indent=4, ensure_ascii=False)
            return True
    except IOError:
        print("Error crítico: No se pudieron guardar los datos en el disco.")
        return False