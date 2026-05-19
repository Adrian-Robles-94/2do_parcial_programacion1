#La funcion se llama: calcular_precio_con_iva


def calcular_precio_con_iva(valor_sin_iva, iva = 21):  # (Parametro obligatorio, parametro opcional) 
    '''Suma el iva al precio, por defecto toma el 21%'''  # Esto es documentacion y es obligatoria para explicar la función
    resultado = valor_sin_iva * (1 + (iva / 100)) # "resultado", es una variable local que contiene la ecuacion de la funcion.
    return resultado # aca retornamos el resultado en su variable local

print(calcular_precio_con_iva(100)) #Al no definir el segundo parametro, se va a ejecutar automaticamente el opcional que armamos. (IVA = 21) = ""121""
print(calcular_precio_con_iva(100, 10)) #Aca definimos el segundo parametro, por lo tanto, no se va ejecutar el opcional = ""110""
