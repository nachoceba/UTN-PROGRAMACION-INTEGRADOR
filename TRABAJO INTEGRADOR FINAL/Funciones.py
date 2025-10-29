def BuscarPaises(nombrepais, paises):

    encontrado = False

    for pais in paises:
        if (
            pais["nombre"].lower() == nombrepais.lower()
            or nombrepais[:3].lower() == pais["nombre"][:3].lower()
        ):
            print(" País encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            encontrado = True

    if encontrado == False:
        print("El país no se encuentra en la lista.")

    return


def FiltrarPaises():

    return


def OrdenarPaises():
    """
    Permite ordenar los países cargados desde 'paises.csv'
    por nombre, población, superficie o continente.
    Muestra los resultados por pantalla de forma clara y segura.
    """

    try:
        archivo = open("paises.csv", "r")  # Abrir el archivo en modo lectura
        archivo.readline()  # salta la primera linea (encabezados)
        paises = []
        for linea in archivo:  # Leer cada línea del archivo
            datos = linea.strip().split(
                ","
            )  # quita saltos de línea y separa por comas, devolviendo una lista datos
            if len(datos) == 4:
                pais = {
                    "nombre": datos[0],
                    "poblacion": int(datos[1]),  # convierte a entero
                    "superficie": int(datos[2]),  # convierte a entero
                    "continente": datos[3],
                }  # crea un diccionario por país
                paises.append(pais)  # agrega el diccionario a la lista de países
        archivo.close()  # Cierra el archivo

    except FileNotFoundError:
        print(" No se encontró el archivo 'paises.csv'.")
        return

    if not paises:
        print(" No hay países cargados para ordenar.")
        return

    # Menú de opciones para ordenar
    print("\nElija cómo desea ordenar los países:")
    print("1) Por nombre")
    print("2) Por población")
    print("3) Por superficie")
    print("4) Por continente")

    # Solicitar opción al usuario
    opcion = input("Ingrese una opción (1-4): ").strip()

    # Si no es una de estas opciones vuelve a pedirla
    while opcion not in ["1", "2", "3", "4"]:
        print("----OPCION INCORRECTA----")
        opcion = input("Ingrese una opción (1-4): ").strip()

    # Preguntar por orden ascendente o descendente
    print("\nDesea ordenar de forma ascendente o descendente?")
    print("A) Ascendente")
    print("D) Descendente")

    orden = input(
        "Ingrese una opción (A/D): "
    ).upper()  # Solicitar opción al usuario y la convierte a mayúscula

    # Si no es una de estas opciones vuelve a pedirla
    while orden not in ["A", "D"]:
        print("----OPCION INCORRECTA----")
        orden = input("Ingrese una opción (A/D): ").upper()

    # Determinar si el orden es descendente
    descendente = orden == "D"

    # Ordenar la lista de países según la opción seleccionada
    # sort ordena y lambda son funciones muy pequeñas que devuelven la clave por la que se va a ordenar
    # se ordena por nombre o población, superficie, continente y se usa lower() para evitar problemas con mayúsculas/minúsculas

    if opcion == "1":
        paises.sort(key=lambda x: x["nombre"].lower(), reverse=descendente)
    elif opcion == "2":
        paises.sort(key=lambda x: x["poblacion"], reverse=descendente)
    elif opcion == "3":
        paises.sort(key=lambda x: x["superficie"], reverse=descendente)
    elif opcion == "4":
        paises.sort(key=lambda x: x["continente"].lower(), reverse=descendente)

    # Mostrar los países ordenados
    print("\n===== LISTA ORDENADA =====")

    # enumerate nos da número (1,2,3...) para mostrar un índice bonito en la salida.
    for i, p in enumerate(paises, start=1):
        print(
            f"{i}. {p['nombre']} - Población: {p['poblacion']} - "
            f"Superficie: {p['superficie']} - Continente: {p['continente']}"
        )
    print("==========================\n")

    return


def MostrarEstadisticas():

    return
