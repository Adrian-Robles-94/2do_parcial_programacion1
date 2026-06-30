import os
import json

def cargar_datos():
    """
    Busca y lee el archivo JSON local para cargar los datos en el programa.
    
    Args:
        Ninguno.
        
    Returns:
        dict: Un diccionario con los datos de los alumnos si el archivo existe,
              o un diccionario vacío si el archivo no es encontrado.
    """
    if os.path.exists("alumnos.json"):
        with open("alumnos.json", "r") as archivo:
            datos = json.load(archivo)
            return datos
    else:
        diccionario_vacio = {}
        return diccionario_vacio

def guardar_datos(alumnos):
    """
    Guarda el diccionario de alumnos de la memoria RAM en el archivo JSON físico.
    
    Args:
        alumnos (dict): El diccionario principal que contiene a todos los estudiantes.
        
    Returns:
        None.
    """
    with open("alumnos.json", "w") as archivo:
        # El parámetro indent=4 hace que el JSON se guarde tabulado y fácil de leer
        json.dump(alumnos, archivo, indent=4)