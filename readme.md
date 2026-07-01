# 📚 SEGUNDO PARCIAL - PROGRAMACIÓN I
**Institución:** UTN Avellaneda  
**Estudiante:** Robles, Maximiliano Adrian  
**Fecha:** 30 de Junio de 2026  
**División:** 316
**DNI:** 38562905

---

## PARTE 1: RESOLUCIÓN DEL CASO DE ESTUDIO (La Biblioteca Digital)

### Parte A - Análisis de Estructuras de Datos
* **Situación 1 (Ubicación en estanterías por filas y columnas):**
  * **Estructura:** Matrices (Listas anidadas en Python).
  * **Justificación:** Es la estructura bidimensional ideal para representar tablas o grillas físicas, permitiendo acceder a cada estante mediante un doble índice numérico `[fila][columna]`.
* **Situación 2 (Información fija de un libro sin modificaciones accidentales):**
  * **Estructura:** Tuplas.
  * **Justificación:** Las tuplas son completamente inmutables en Python. Una vez definidas, sus elementos no pueden alterarse en tiempo de ejecución, garantizando la integridad de datos fijos como el ISBN o el autor.
* **Situación 3 (Evitar el registro de socios duplicados):**
  * **Estructura:** Conjuntos (`set`).
  * **Justificación:** Los conjuntos matemáticos en Python descartan de forma nativa y automática cualquier elemento repetido, asegurando que cada socio sea único sin necesidad de lógica extra.
* **Situación 4 (Relacionar un ISBN con toda la información de un libro):**
  * **Estructura:** Diccionarios.
  * **Justificación:** Funcionan mediante el modelo asociativo clave-valor. Usar el ISBN como clave única permite mapear y recuperar instantáneamente el bloque de datos del libro.
* **Situación 5 (Conservar la información al cerrar el programa):**
  * **Estructura:** Archivos (formato JSON).
  * **Justificación:** Proporcionan persistencia a largo plazo al escribir los datos en el almacenamiento secundario (disco duro) en vez de la memoria volátil (RAM).

### Parte B - Razonamiento Teórico
1. **Múltiples listas separadas para datos relacionados:** Es propenso a errores críticos de consistencia. Si un elemento se elimina, modifica o desordena en una lista, se rompe la sincronización de índices con las demás listas, corrompiendo la relación de los datos.
2. **Ventajas de la estructura clave-valor para búsquedas:** Ofrece una velocidad de acceso directo en tiempo constante promedio. No requiere recorrer secuencialmente la estructura con bucles `for`, optimizando el rendimiento.
3. **Utilidad de no permitir duplicados en sistemas reales:** Previene la redundancia de datos y asegura la unicidad de registros críticos del negocio como documentos de identidad (DNI), pasaportes o correos electrónicos de usuarios.
4. **Memoria (RAM) vs. Archivos (Disco):**
  * *Memoria:* Es volátil y ultra rápida; los datos se pierden al apagar el sistema. Se usa para variables temporales y procesamiento activo.
  * *Archivos:* Son permanentes y no volátiles. Se utilizan para bases de datos, configuraciones e históricos que deben trascender el ciclo de vida del programa.

### Parte C - Análisis de Código
1. **Fragmento de la Tupla (`libro[1] = "Python Avanzado"`):**
  * *¿Funcionará?* No.
  * *¿Qué ocurrirá?* Lanzará un error de tipo `TypeError: 'tuple' object does not support item assignment` en la consola.
  * *¿Por qué?* Por la propiedad de **inmutabilidad** de las tuplas, la cual prohíbe explícitamente reasignar valores a sus índices ya creados.
2. **Fragmento del Conjunto (`socios = {"Juan", "Ana", "Pedro", "Ana"}`):**
  * *Cantidad de elementos:* Contendrá estrictamente 3 elementos.
  * *¿Por qué?* El elemento `"Ana"` está duplicado y el `set` descarta automáticamente las repeticiones.
  * *Ventaja:* Optimiza la memoria y garantiza la unicidad de datos de forma nativa sin algoritmos de filtrado manuales.
3. **Fragmento del Diccionario Anidado (`libros = { "9789501234567": {...} }`):**
  * *Estructura:* Es un Diccionario anidado (un diccionario cuyos valores son otros diccionarios).
  * *Representación de las claves:* La clave principal es el ISBN del libro (identificador único), y las claves internas representan las propiedades específicas como `titulo` y `autor`.
  * *Ventaja para búsquedas:* Permite un acceso instantáneo a la ficha técnica del libro con una sola operación (`libros[isbn]`), sin iterar.
4. **Discusión sobre la afirmación: "Se puede resolver todo solo con listas"**
  * *Postura:* Desacuerdo parcial.
  * *Análisis:* Técnicamente es posible simular otras estructuras con listas, pero es altamente ineficiente. Las búsquedas requieren recorrer todos los elementos, no impiden duplicados nativamente y complejizan exponencialmente el mantenimiento del código, provocando sistemas frágiles.

---

## PARTE 2: RESOLUCIÓN DEL MÚLTIPLE CHOICE

A continuación se transcriben las preguntas completas del examen junto con la selección de opciones correctas y sus correspondientes fundamentos técnicos:

### 1. Respecto a los diccionarios en Python:
**A.** Permiten almacenar información mediante pares clave-valor.  
**B.** Las claves deben ser únicas.  
**C.** Los diccionarios mantienen el orden únicamente si se utiliza sorted().  
**D.** Se puede acceder a un valor utilizando su clave.  
**E.** Los diccionarios no permiten almacenar otros diccionarios.  
**F.** Son útiles para representar entidades como alumnos, libros o productos.  

> **Respuesta**: A, B, D, F  

---

### 2. Respecto a las tuplas:
**A.** Son estructuras mutables.  
**B.** Permiten almacenar distintos tipos de datos.  
**C.** Una vez creadas, sus elementos no pueden modificarse.  
**D.** Son adecuadas para representar información que no debería cambiar.  
**E.** Siempre ocupan más memoria que las listas.  
**F.** Admiten acceso mediante índices.  

> **Respuesta**: B, C, D, F  

---

### 3. Respecto a los conjuntos (set):
**A.** Permiten elementos duplicados.  
**B.** Son útiles para eliminar elementos repetidos.  
**C.** No garantizan posiciones mediante índices.  
**D.** Permiten acceder a sus elementos utilizando índices.  
**E.** Son adecuados para representar colecciones de elementos únicos.  
**F.** Mantienen necesariamente el orden de inserción.  

> **Respuesta**: B, C, E  

---

### 4. Respecto a las matrices en Python:
**A.** Generalmente se representan mediante listas anidadas.  
**B.** Son adecuadas para modelar información organizada en filas y columnas.  
**C.** Son una estructura nativa específica de Python llamada matrix.  
**D.** No pueden recorrerse mediante ciclos.  
**E.** Todos sus elementos deben ser del mismo tipo.  
**F.** Permiten acceder a una posición utilizando fila y columna.  

> **Respuesta**: A, B, F  

---

### 5. Respecto al manejo de archivos:
**A.** Permite conservar información luego de finalizar la ejecución del programa.  
**B.** El modo "r" se utiliza para lectura.  
**C.** El modo "w" permite escribir en un archivo.  
**D.** Los datos almacenados en archivos desaparecen cuando el programa finaliza.  
**E.** La instrucción with open(...) ayuda a gestionar correctamente el cierre del archivo.  
**F.** Los archivos solo pueden almacenar texto.  

> **Respuesta**: A, B, C, E  

---

### 6. Respecto a las funciones como ciudadanos de primera clase:
**A.** Pueden almacenarse en variables.  
**B.** Pueden pasarse como argumentos a otras funciones.  
**C.** Pueden retornarse desde otras funciones.  
**D.** Solo pueden ejecutarse directamente por su nombre original.  
**E.** No pueden almacenarse dentro de estructuras de datos.  
**F.** Este comportamiento permite construir programas más reutilizables y flexibles.  

> **Respuesta**: A, B, C, F  

---

## PARTE 3: DOCUMENTACIÓN DEL SISTEMA DE GESTIÓN DE ALUMNOS (README)

Este bloque detalla el diseño de software y la implementación práctica aplicados en el desarrollo de la aplicación de gestión modular, cumpliendo con los criterios requeridos para alcanzar la Instancia de Aprobación Directa.

### 📁 Estructura del Proyecto y Modularización
El sistema se diseñó bajo el principio de responsabilidad única, distribuyendo la lógica en un paquete modular estructurado de la siguiente forma:

```text
proyecto/
│
├── main.py            # Punto de entrada único del programa. Controla el flujo del menú principal.
├── alumnos.py         # Módulo de negocio. Contiene el ABM (Alta, Baja, Modificación) y listados.
├── archivos.py        # Módulo de persistencia. Gestiona la lectura y escritura en disco.
├── validaciones.py    # Módulo de control. Sanitiza y valida las entradas de datos del usuario.
├── estadisticas.py    # Módulo de cómputo. Procesa métricas, promedios y máximos académicos.
└── alumnos.json       # Archivo de persistencia de datos en formato JSON de almacenamiento persistente.