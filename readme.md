# 📚 SEGUNDO PARCIAL - PROGRAMACIÓN I
**Institución:** UTN Avellaneda  
**Estudiante:** Robles, Maximiliano Adrian
**Fecha:** 30 de Junio de 2026  

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
2. **Ventajas de la estructura clave-valor para búsquedas:** Ofrece una velocidad de acceso directo en tiempo constante promedio $O(1)$. No requiere recorrer secuencialmente la estructura con bucles `for`, optimizando el rendimiento.
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

A continuación se detallan las opciones técnicamente correctas para cada temática junto a su respectivo fundamento conceptual:

### 1. Respecto a los diccionarios en Python

* **Opciones seleccionadas como CORRECTAS:**
    * **[A]** "Permiten almacenar información mediante pares clave-valor."
    * **[B]** "Las claves deben ser únicas."
    * **[D]** "Se puede acceder a un valor utilizando su clave."
    * **[F]** "Son útiles para representar entidades como alumnos, libros o productos."

* **Justificación:** Los diccionarios implementan el tipo asociativo en Python. Exigen la unicidad de claves para evitar ambigüedades en las búsquedas directas y son ideales para representar registros o entidades de la vida real. Las opciones C y E son falsas porque los diccionarios modernos preservan el orden de inserción por defecto y soportan perfectamente la anidación de otras estructuras en sus valores.

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

``
> **Justificación**: Los diccionarios implementan el modelo asociativo en Python. Exigen que las claves sean únicas para poder recuperar los valores asociados de forma directa y eficiente sin ambigüedades. Son la estructura ideal para mapear registros o entidades del mundo real. Las opciones C y E son falsas porque las versiones modernas de Python preservan el orden de inserción por defecto y los diccionarios admiten perfectamente la anidación de otras estructuras complejas dentro de sus valores.
``

---

### 2. Respecto a las tuplas:

**A.** Son estructuras mutables.

**B.** Permiten almacenar distintos tipos de datos.

**C.** Una vez creadas, sus elementos no pueden modificarse.

**D.** Son adecuadas para representar información que no debería cambiar.

**E.** Siempre ocupan más memoria que las listas.

**F.** Admiten acceso mediante índices.

> **Respuesta**: B, C, D, F

> **Justificación**: La principal característica técnica de una tupla es su inmutabilidad, lo que garantiza que sus elementos no puedan ser alterados ni reasignados en tiempo de ejecución una vez definidos, protegiendo los datos fijos. Además, permiten colecciones de datos heterogéneos y se accede a ellos a través de índices numéricos enteros. La opción A es falsa por la naturaleza misma de la estructura y la E es incorrecta porque, al ser estáticas, optimizan el espacio y consumen menos memoria que una lista.

---

### 3. Respecto a los conjuntos (set):

**A.** Permiten elementos duplicados.

**B.** Son útiles para eliminar elementos repetidos.

**C.** No garantizan posiciones mediante índices.

**D.** Permiten acceder a sus elementos utilizando índices.

**E.** Son adecuados para representar colecciones de elementos únicos.

**F.** Mantienen necesariamente el orden de inserción.

> **Respuesta**: B, C, E

> **Justificación**: Los conjuntos matemáticos "set" están diseñados específicamente para almacenar elementos únicos, descartando de forma automática cualquier ingreso duplicado en la colección. Debido a que su ordenamiento interno está basado en tablas de hash para búsquedas veloces, carecen de un orden posicional fijo. Por este motivo, las opciones A, D y F son falsas: no toleran duplicados, no respetan el orden de entrada y cualquier intento de acceder mediante corchetes e índices producirá un error de tipo "TypeError".

---

### 4. Respecto a las matrices en Python:

**A.** Generalmente se representan mediante listas anidadas.

**B.** Son adecuadas para modelar información organizada en filas y columnas.

**C.** Son una estructura nativa específica de Python llamada matrix.

**D.** No pueden recorrerse mediante ciclos.

**E.** Todos sus elementos deben ser del mismo tipo.

**F.** Permiten acceder a una posición utilizando fila y columna.

> **Respuesta**: A, B, F

> **Justificación**: Python no cuenta con un tipo de dato primitivo integrado llamado "matrix", por lo que la forma estándar de representarlas es a través de listas anidadas (listas que contienen otras listas). Esto permite modelar estructuras bidimensionales de filas y columnas, accediendo a sus celdas mediante la sintaxis de doble índice "matriz[fila][columna]". Las opciones C, D y E son incorrectas ya que no es un tipo nativo, se recorren de manera simple con bucles "for" anidados y sus elementos pueden ser de tipos mixtos.

---

### 5. Respecto al manejo de archivos:

**A.** Permite conservar información luego de finalizar la ejecución del programa.

**B.** El modo "r" se utiliza para lectura.

**C.** El modo "w" permite escribir en un archivo.

**D.** Los datos almacenados en archivos desaparecen cuando el programa finaliza.

**E.** La instrucción with open(...) ayuda a gestionar correctamente el cierre del archivo.

**F.** Los archivos solo pueden almacenar texto.

> **Respuesta**: A, B, C, E

> **Justificación**: Los archivos ofrecen persistencia en el almacenamiento secundario, logrando que la información se conserve intacta al cerrar el sistema. Los caracteres "r" y "w" definen las operaciones nativas de lectura y escritura (origen de "read" y "write"), mientras que el administrador de contexto "with" asegura que el archivo se cierre correctamente en el sistema operativo ante cualquier eventualidad o fallo. Las opciones D y F son falsas porque los datos son permanentes y los archivos pueden almacenar datos binarios, imágenes o estructuras serializadas como archivos JSON.

---

### 6. Respecto a las funciones como ciudadanos de primera clase:

**A.** Pueden almacenarse en variables.

**B.** Pueden pasarse como argumentos a otras funciones.

**C.** Pueden retornarse desde otras funciones.

**D.** Solo pueden ejecutarse directamente por su nombre original.

**E.** No pueden almacenarse dentro de estructuras de datos.

**F.** Este comportamiento permite construir programas más reutilizables y flexibles.

> **Respuesta**: A, B, C, F

> **Justificación**: Que las funciones sean consideradas "ciudadanos de primera clase" significa que el lenguaje las trata con los mismos derechos que a cualquier otro objeto (como enteros o cadenas). Esto permite asignarlas a variables para usarlas con alias, pasarlas como parámetros a otras funciones (técnica conocida como "callbacks") o devolverlas como resultado de un proceso. Las opciones D y E son incorrectas porque rompen este principio fundamental al negar que se puedan guardar en estructuras o invocar mediante referencias alternativas.