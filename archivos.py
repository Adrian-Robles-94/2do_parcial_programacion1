import json
import os

def cargar_alumnos(ruta_archivo: str) -> dict:
    """
    Carga los datos del archivo JSON. Si el archivo no existe,
    gestiona la excepción retornando un diccionario vacío.
    """
    if not os.path.exists(ruta_archivo):
        return {}
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, IOError):
        return {}

def guardar_alumnos(ruta_archivo: str, diccionario_alumnos: dict) -> bool:
    """
    Guarda de forma persistente la información en formato JSON.
    """
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(diccionario_alumnos, archivo, indent=4, ensure_ascii=False)
            return True
    except IOError:
        print("Error: No se pudo escribir en el archivo de almacenamiento.")
        return False