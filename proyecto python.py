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
        exit()
data=cargar_datos()
# ------------------- #
# Función de filtro de busqueda por nombre
def filtro_nombre(datos):
    strFiltro=input("Introduce el nombre que desea buscar: ") #Variable que almacena el nombre del lanzamiento
    encontrado=False # Variable que indica si se ha encontrado el lanzamiento o no
    indice_registro=0 # Variable que almacena el indice de todos los lanzamientos

# Bucle que revisa todos los lanzamientos y termina si se acaba la lista o se ha encontrado el lanzamiento
    while(indice_registro<len(datos)-1 and encontrado==False):
        #Si el nombre coincide con el del lanzamiento actual, almacena todos los datos del lanzamiento en una variable y termina el proceso de busqueda
        if(strFiltro.upper()==datos[indice_registro].get("name").upper()):
            lanzamiento=datos[indice_registro]
            encontrado=True
            fechaLanzamiento=lanzamiento.get("date_utc") # Almacena la fecha de lanzamiento en una variable
            #Mostramos los datos
            print("#---------------#")
            print("DATOS: ")
            print(" Nº de lanzamiento: ", lanzamiento.get("flight_number"))
            print(" Nombre: ",lanzamiento.get("name"))
            print(" Fecha de lanzamiento (UTC - YYYY/MM/DD): ", fechaLanzamiento[:10].replace("-","/")) #Mostramos la fecha sin los datos horarios
            if(lanzamiento.get("success")==False):
                print(" Exito en lanzamiento: No exitoso")
                print("\t Detalles: ", lanzamiento.get("details"))
            print("#---------------#")
        else: # En el caso de que no coincida, aumenta el indice de busqueda de lanzamiento y hace el mismo procedimiento en el siguiente
                indice_registro+=1
    if(encontrado==False):
        print("EL lanzamiento no se encuentra entre los datos actuales.")

# ------------------- #
# Función de filtro de busqueda por nº de lanzamiento #
def filtro_numero(datos):
    encontrado=False
    ultimoLanzamiento=datos[len(datos)-1].get("flight_number")
    intFiltro=int(input("Introduzca el nº del lanzamiento del que quiere saber los datos (1 - %d) "%(ultimoLanzamiento)))-1
    if(intFiltro<len(datos)-1 and encontrado==False):
        print("#---------------#")
        print("DATOS: ")
        print(" Nº de lanzamiento: ", datos[intFiltro].get("flight_number"))
        print(" Nombre: ",datos[intFiltro].get("name"))
        print(" Fecha de lanzamiento (UTC - YYYY/MM/DD): ", datos[intFiltro].get("date_utc")[:10].replace("-","/")) #Mostramos la fecha sin los datos horarios
        if(datos[intFiltro].get("success")==False):
            print(" Exito en lanzamiento: No exitoso")
            print("\t Detalles: ", datos[intFiltro].get("details"))
        else:
            print(" Exito en lanzamiento: Exitoso")
        print("#---------------#")

# ------------------- #
#Creamos la función que muestra el menu
def mostrar_menu():
   
   # Opciones del menu #
    print("1 ¬ Buscar por nombre")
    print("2 ¬ Buscar por número de lanzamiento")
    #Solicitamos entrada de opción
    opcion=int(input("Introduce tu opción: "))
    continuar=True

    try:
        if(opcion>=1 and opcion<=2): #Comprobamos que es una opción valida
            if(continuar): #Comprobamos si tras la consulta, quiere hacer otra.
                #Comprobamos que opción introduce, y ejecuta la función correspondiente.
                if(opcion==1): 
                    filtro_nombre(data) # Llamamos a la funcion de filtrar por el nombre, a la que le pasamos como paramentro los datos del JSON almacenados en un diccionario
                if(opcion==2):
                    filtro_numero(data) # Llamamos a la funcion de filtrar por numero de lanzamiento y le pasamos como parametro los datos del JSON almacenados en un diccionario
        else:
            print("Introduzca una opción valida.")
    except ValueError:
        print("Introduzca una opción valida")
    # Tras la busqueda, preguntamos si quiere realizar una distinta
    if(input("¿Quiere hacer otra busqueda? (S/N)").upper()=="S"): # En caso afirmativo, llama de nuevo a la función del menú
        mostrar_menu()
    else: # En caso negativo, se finaliza el programa mostrando como condigo de salida un 0 (salida voluntaria del programa)
        print("Programa finalizado")
        exit(0)
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