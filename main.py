from utilidades import (
    mostrar_menu,
    pedir_opcion_menu
)

from validaciones import (
    pedir_contrasena
)

from analisis import (
    validar_nivel_seguridad,
    buscar_caracter,
    mostrar_contrasena_invertida,
    verificar_palindromo
)

from estadisticas import (
    contar_tipos_caracteres,
    generar_reporte_estadistico
)


def main() -> None:
    """
    Función principal del programa.
    Controla el menú y las funcionalidades.
    """

    contrasena = ""

    while True:

        mostrar_menu()

        opcion = pedir_opcion_menu()

        if opcion == 1:

            contrasena = pedir_contrasena()

            print("\nContraseña guardada correctamente.")

        elif opcion == 2:

            if contrasena == "":
                print(
                    "\nPrimero debe ingresar "
                    "una contraseña."
                )

            else:
                validar_nivel_seguridad(contrasena)

        elif opcion == 3:

            if contrasena == "":
                print(
                    "\nPrimero debe ingresar "
                    "una contraseña."
                )

            else:
                contar_tipos_caracteres(contrasena)

        elif opcion == 4:

            if contrasena == "":
                print(
                    "\nPrimero debe ingresar "
                    "una contraseña."
                )

            else:

                caracter = input(
                    "\nIngrese un carácter a buscar: "
                )

                buscar_caracter(
                    contrasena,
                    caracter
                )

        elif opcion == 5:

            if contrasena == "":
                print(
                    "\nPrimero debe ingresar "
                    "una contraseña."
                )

            else:
                mostrar_contrasena_invertida(
                    contrasena
                )

        elif opcion == 6:

            if contrasena == "":
                print(
                    "\nPrimero debe ingresar "
                    "una contraseña."
                )

            else:
                generar_reporte_estadistico(
                    contrasena
                )

        elif opcion == 7:

            if contrasena == "":
                print(
                    "\nPrimero debe ingresar "
                    "una contraseña."
                )

            else:
                verificar_palindromo(
                    contrasena
                )

        elif opcion == 8:

            print(
                "\nLa funcionalidad de ordenamiento "
                "todavía no fue implementada."
            )

        elif opcion == 9:

            print("\nPrograma finalizado.")
            break


main()