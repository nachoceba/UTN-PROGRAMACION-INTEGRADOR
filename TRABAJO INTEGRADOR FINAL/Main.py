"""
Objetivo
Desarrollar una aplicación en Python que permita gestionar información sobre países,
aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas,
ordenamientos y estadísticas. El sistema debe ser capaz de leer datos desde un archivo CSV,
realizar consultas y generar indicadores clave a partir del dataset.
El objetivo principal es afianzar el uso de estructuras de datos, modularización con funciones
y técnicas de filtrado/ordenamiento, aplicando los conceptos aprendidos en Programación 1.

"""
from Funciones import BuscarPaises

from Funciones import FiltrarPaises

from Funciones import OrdenarPaises

from Funciones import MostrarEstadisticas


#Creamos una funcion que valide las opciones del programa
def ValidarOpcion (seguirprograma):

    while seguirprograma not in ["S","N"]:
            print("----OPCION INCORRECTA----")
            seguirprograma = input("Ingrese una opcion: ").upper()
    
    return seguirprograma

#Creamos el archivo CSV con los paises dichos en el TP
try:
    open("paises.csv", "x").write(
        "nombre,poblacion,superficie,continente\n"
        "Argentina,45376763,2780400,America\n"
        "Japon,125800000,377975,Asia\n"
        "Brasil,213993437,8515767,America\n"
        "Alemania,83149300,357022,Europa\n"
    )
except FileExistsError:
    pass

#Creamos una funcion con la carga de los paises dentro de una lista de diccionarios

def CargarPaises():
    paises = []

    with open("paises.csv", "r") as archivo:
        archivo.readline() 

        for linea in archivo:
            datos = linea.strip().split(",")

            pais = {
                "nombre": datos[0],
                "poblacion": int(datos[1]),
                "superficie": int(datos[2]),
                "continente": datos[3]
            }

            paises.append(pais)

    return paises


#Inicializamos las variables principales del programa

nombrepais = ""

poblacion = 0

superficie = 0

continente = ""

seguirprograma = "S"

opcion = ""

opciones = ["A","B","C","D","E"]

print("=====================================================================")
print("          BIENVENIDO AL PROGRAMA SOBRE LA GESTION DE PAISES")
print("=====================================================================")


while seguirprograma == "S":
    
    paises = CargarPaises()
    
    print("Estas en el menu principal, a continuacion elija la opcion que desee: ")
    print("----------------------------------------------------------------------")
    
    print("A) Si desea buscar algun pais dentro del programa ")
    print("B) Si desea filtrar los paises segun caracteristicas ")
    print("C) Si desea ordenar los paises ")
    print("D) Mostrar estadisticas ")
    print("E) Si desea salir del programa ")
    
    opcion = input("Ingrese una opcion: ").upper()

    #Corroboramos con un while que la opcion sea alguna de las mostradas por pantalla, si no es asi repite y muestra error hasta arreglarlo

    while opcion not in opciones:
        print("----OPCION INCORRECTA----")
        opcion = input("Ingrese una opcion correcta: ").upper()


    if opcion == "E":
        seguirprograma = "N"

    if opcion == "A":
        print("----------------------------------------------------------------------")
        print("Usted ha ingresado al apartado buscar paises ")
        
        nombrepais = input("Ingrese el nombre del pais que quiere buscar: ")

        BuscarPaises(nombrepais,paises)

        print("----------------------------------------------------------------------")
        print("¿Desea regresar al menu? (Escriba S para seguir o N para salir)")

        seguirprograma = input("Ingrese una opcion: ").upper()
        seguirprograma = ValidarOpcion(seguirprograma)

    if opcion == "B":
        print("----------------------------------------------------------------------")
        print("Usted ha ingresado al apartado de filtrar paises")

        FiltrarPaises()
        print("¿Desea regresar al menu? (Escriba S para seguir o N para salir)")
        seguirprograma = input("Ingrese una opcion: ").upper()
        seguirprograma = ValidarOpcion(seguirprograma)

    if opcion == "C":
        print("----------------------------------------------------------------------")
        print("Usted ha ingresado al apartado de ordenar paises")

        OrdenarPaises()

        print("¿Desea regresar al menu? (Escriba S para seguir o N para salir)")
        seguirprograma = input("Ingrese una opcion: ").upper()
        seguirprograma = ValidarOpcion(seguirprograma)

    if opcion == "D":
        print("----------------------------------------------------------------------")
        print("A continuacion las estadisticas de los paises ")

        MostrarEstadisticas()

        print("¿Desea regresar al menu? (Escriba S para seguir o N para salir)")
        seguirprograma = input("Ingrese una opcion: ").upper()
        seguirprograma = ValidarOpcion(seguirprograma)


        


print("----------------------------------------------------------------------")
print("Usted ha salido del programa, vuelva pronto. ")

