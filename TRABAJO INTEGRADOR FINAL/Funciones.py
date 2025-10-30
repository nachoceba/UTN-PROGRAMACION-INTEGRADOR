def BuscarPaises(nombrepais, paises):

    encontrado = False

    for pais in paises:
        if (pais["nombre"].lower() == nombrepais.lower()or nombrepais[:3].lower() == pais["nombre"][:3].lower()):

            print(" País encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            encontrado = True

    if encontrado == False:
        print("El país no se encuentra en la lista.")

    return


def FiltrarPaises(paises):
    
    rangomenor = 0
    rangomayor = 0
    encontrado = False
    continente = ""

    print("¿Por qué criterio desea filtrar los países?")
    print("A) Población")
    print("B) Superficie")
    print("C) Continente")
    print("D) Salir")

    opcion = input("Ingrese una opción: ").upper()

    #Validamos que la respuesta ingresada sea una de las pedidas con un while
    while opcion not in ["A", "B", "C","D"]:
        print("---- OPCIÓN INCORRECTA ----")
        opcion = input("Ingrese una opción válida: ").upper()

    if opcion == "A":
        print("------------------------------------------------------------")
        print("Accediste a filtrar por poblacion ")
        
        # Pedir mínimo
        rangomenor = input("Por favor ingrese el mínimo de población de los países a buscar: ")

        #Valido que solo si ingresen numeros y no otro caracter
        while not rangomenor.isdigit():
            print("ERROR, INGRESE UNA OPCIÓN VÁLIDA (solo números enteros)")
            rangomenor = input("Por favor ingrese el mínimo de población de los países a buscar: ")

        rangomenor = int(rangomenor)


        # Pedir máximo
        rangomayor = input("Por favor ingrese el máximo de población de los países a buscar: ")

        #Valido que solo si ingresen numeros y no otro caracter
        while not rangomayor.isdigit():
            print("ERROR, INGRESE UNA OPCIÓN VÁLIDA (solo números enteros)")
            rangomayor = input("Por favor ingrese el máximo de población de los países a buscar: ")

        rangomayor = int(rangomayor)


        for pais in paises:
            if (pais["poblacion"] >= rangomenor and pais["poblacion"] <= rangomayor):
                print("-------------------")
                print("")
                print(" País encontrado:")
                print(f"Nombre: {pais['nombre']}")
                print(f"Población: {pais['poblacion']}")
                print("")
                encontrado = True

        if encontrado == False:
            print("No hay ningun pais con los rangos ingresados ")
    
    if opcion == "B":
        print("---------------------------------------------------------------")
        print("Accediste a filtrar por superficie ")

        # Pedir mínimo
        rangomenor = input("Por favor ingrese el mínimo de superficie de los países a buscar: ")

        #Valido que solo si ingresen numeros y no otro caracter
        while not rangomenor.isdigit():
            print("ERROR, INGRESE UNA OPCIÓN VÁLIDA (solo números enteros)")
            rangomenor = input("Por favor ingrese el mínimo de población de los países a buscar: ")

        rangomenor = int(rangomenor)


        # Pedir máximo
        rangomayor = input("Por favor ingrese el máximo de superficie de los países a buscar: ")

        #Valido que solo si ingresen numeros y no otro caracter
        while not rangomayor.isdigit():
            print("ERROR, INGRESE UNA OPCIÓN VÁLIDA (solo números enteros)")
            rangomayor = input("Por favor ingrese el máximo de población de los países a buscar: ")

        rangomayor = int(rangomayor)


        for pais in paises:
            if (pais["superficie"] >= rangomenor and pais["superficie"] <= rangomayor):
                print("-------------------")
                print(" País encontrado:")
                print("")
                print(f"Nombre: {pais['nombre']}")
                print(f"Superficie: {pais['superficie']}")
                print("")
                encontrado = True

        if encontrado == False:
            print("No hay ningun pais con los rangos ingresados ")
    
    
    if opcion == "C":
        print("---------------------------------------------------------------")
        print("Accediste a filtrar por continente ")

        #Pedir continente a filtrar
        continente = input("Ingrese el continente por el cual queres que se filtren los paises (Ingrese el continente sin tildes): ").lower()
        
        #Validamos que ingrese un continente correcto
        while continente not in ["asia","oceania","america","europa","africa"]:
           print("ERROR, EL CONTINENTE INGRESADO NO COINCIDE CON NINGUNO ")
           continente = input("Ingrese el continente por el cual queres que se filtren los paises(Ingrese el continente sin tildes): ").lower()
        
        for pais in paises:
            if (pais["continente"].lower() == continente.lower()):
                print("-------------------")
                print(" País encontrado:")
                print("")
                print(f"Nombre: {pais['nombre']}")
                print(f"Continente: {pais['continente']}")
                print("")
                encontrado = True
        
        
        if encontrado == False:
            print("No hay paises en el sistema con ese continente ")

    if opcion == "D":
        print("Saliendo del apartado filtros......")
        return


def OrdenarPaises(paises):
   
    print("¿Por qué criterio desea ordenar los países?")
    print("A) Nombre")
    print("B) Población")
    print("C) Superficie")
    print("D) Continente")
    print("E) Salir")

    opcion = input("Ingrese una opción: ").upper()

    #Validamos que la respuesta ingresada sea una de las pedidas con un while
    while opcion not in ["A", "B", "C", "D", "E"]:
        print("---- OPCIÓN INCORRECTA ----")
        opcion = input("Ingrese una opción válida: ").upper()

    # Elegimos el campo a usar según la opción
    if opcion == "A":
        clave = "nombre"
    elif opcion == "B":
        clave = "poblacion"
    elif opcion == "C":
        clave = "superficie"
    else:
        clave = "continente"

    # Preguntamos si quiere ascendente o descendente
    print("¿Cómo desea ordenar?")
    print("1) Ascendente (menor a mayor)")
    print("2) Descendente (mayor a menor)")

    tipo = input("Ingrese 1 o 2: ")

    #Validamos que la respuesta ingresada sea una de las pedidas con un while
    while tipo not in ["1", "2"]:
        print("---- OPCIÓN INCORRECTA ----")
        tipo = input("Ingrese 1 o 2: ")


    n = len(paises)
    #Utilizamos el ordenamiento tipo burbuja visto en los videos del campus
    for i in range(n - 1):
        #En el for de j le restamos 1 y ademas el indice para que solo revise los paises que faltan ordenar y no revise toda la lista en cada iteracion.
        for j in range(n - 1 - i):
            if tipo == "1":  # Ascendente
                if paises[j][clave] > paises[j + 1][clave]:
                    #Aca realizamos el cambio una vez sabemos cual es mayor
                    aux = paises[j]#Lo guardamos en una variable auxiliar para facilitar el cambio
                    paises[j] = paises[j + 1]
                    paises[j + 1] = aux
            else:  # Decreciente
                if paises[j][clave] < paises[j + 1][clave]:
                    #Aca realizamos el cambio una vez sabemos cual es menor
                    aux = paises[j]#Lo guardamos en una variable auxiliar para facilitar el cambio
                    paises[j] = paises[j + 1]
                    paises[j + 1] = aux

    print("------------------------------------------------------------")
    print(f"Países ordenados por {clave.upper()}:")
    print("------------------------------------------------------------")

    for pais in paises:
         print(f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")

    print("------------------------------------------------------------")

    if opcion == "E":
        print("Saliendo del apartado ordenar paises.... ")
        return



def MostrarEstadisticas():

    return
