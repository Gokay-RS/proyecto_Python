#Importamos las bibliotecas necesarias
import requests

# --- <FUNCIONES> --- #
#Creamos la función para descargar los datos de los lanzamientos desde la API de SpaceX
def cargar_datos():
    url="https://api.spacexdata.com/v4/launches"
    
    try:
        response=requests.get(url) # Descargamos los datos de lanzamiento desde la API de SpaceX
        response.raise_for_status() # Se comprueba si la solicitud a sido exitosa, en caso negativo captura el error y lo muestra mas alante
        datos=response.json() #Almacenamos los datos en un diccionario
        return datos # Devuelve los datos almacenados en un diccionario
    except requests.exceptions.RequestException as error: # Si la solicitud falla, muestra el siguiente mensaje
        print("Error al cargar los datos.\nCódigo de error: ", error) # Muestra por pantalla el mensaje de error, junto con el código
        exit(0) # Sale devolviendo el error 
# ------------------- #
def filtro_nombre(datos):
    strFiltro=input("Introduce el nombre que desea buscar: ")
    encontrado=False
    indice_registro=0
    indice_lanzamiento=0

    while(indice_registro<len(datos) and encontrado==False):
        while(indice_lanzamiento<(len(datos[indice_registro]) and encontrado==False)):
            if(strFiltro==datos[indice_registro].get("name")):
                lanzamiento=datos[indice_registro]
                encontrado=True
            else:
                indice+=1

    fechaLanzamiento=lanzamiento.get("date_utc")

    print("DATOS: ")
    print(" Nombre: ",lanzamiento.get("name"))
    print(" Fecha de lanzamiento (UTC): ", fechaLanzamiento[:10])

# ------------------- #
#Creamos la función que muestra el menu
def mostrar_menu():
   
    print("1 ¬ Buscar por nombre")
    opcion=int(input("Introduce tu opción: "))
    continuar=True    

    if(opcion>=1 or continuar):
        if(opcion==1):
            filtro_nombre(cargar_datos())
    
    if(input("¿Quiere hacer otra busqueda? (S/N)").upper()=="S"):
        mostrar_menu()
    else:
        print("Programa finalizado")
        exit(1)
# ------------------- #
# Funcion para mostrar el nombre del proyecto de python
def mostrar_titulo():
    nombrePrograma="""
  #####                                       ##  ##             ###                                            |
 ##   ##                                      ##  ##              ##                                            |
 #        ######    ####     ####     ####     ####    ######     ##      ####    ######    ####    ######      |
  #####    ##  ##      ##   ##  ##   ##  ##     ##      ##  ##    ##     ##  ##    ##  ##  ##  ##    ##  ##     |
      ##   ##  ##   #####   ##       ######    ####     ##  ##    ##     ##  ##    ##      ######    ##         |
 ##   ##   #####   ##  ##   ##  ##   ##       ##  ##    #####     ##     ##  ##    ##      ##        ##         |
  #####    ##       #####    ####     #####   ##  ##    ##       ####     ####    ####      #####   ####        |
          ####                                         ####                                                     |
                                                                                                                |"""
    print(nombrePrograma)
    print("_________________________________________________________________________________________________________________")
# ------------------- #
mostrar_titulo()
mostrar_menu()