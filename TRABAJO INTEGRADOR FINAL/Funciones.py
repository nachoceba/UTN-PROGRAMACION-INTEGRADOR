def BuscarPaises(nombrepais,paises):
    
    encontrado = False

    for pais in paises:
        if pais["nombre"].lower() == nombrepais.lower() or nombrepais[:3].lower() == pais["nombre"][:3].lower():
            print("✅ País encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            encontrado = True
            
        

    if encontrado == False:
        print("❌ El país no se encuentra en la lista.")

    return 


def FiltrarPaises():

    return

def OrdenarPaises():

    return

def MostrarEstadisticas():

    return

