


#****************************************************************************************************
#buscar un indice disponible

def buscar_indice_disponible(lista_estados):
#proposito : devuelve el indice disponible de una lista.
        #  *EN CASO DE NO HABER INDICE DISPONIBLE RETORNA FALSE*
#parametro : lista_estados/lista ingresada de estados

    contador = 0
    resultado = None
    for i in range(len(lista_estados)):        
        if lista_estados[i] == 0 and contador == 0:
            contador +=1
            resultado = i
    if contador == 0:
        resultado = False
    return(resultado)

# ingresa un dato en el indice que quiera

def ingresar_en_indice(lista_ingresada, elemento, indice):
    """
    proposito: modifica el elemento del indice dado por el elemento dado en la lista dada.
    parametros: lista_ingresada/lista a modificar
                elemento/elemento por el que se reemplaza el elemento con el indice dado
                indice/indice del elemento
    """
    for i in range(len(lista_ingresada)):
        if i == indice:
            lista_ingresada[i] = elemento
#****************************************************************************************************


#****************************************************************************************************
#imprimir una matriz

def imprimir_fila(fila_ingresada):
# proposito: imprime una lista como fila visual de matriz.
# parametro: fila_ingresada/ fila a imprimir en formato matriz.
    salida = ""

    for i in range(len(fila_ingresada)):
        if i == 0:
            salida += "|"
            salida += str(fila_ingresada[i])
           
        elif i == len(fila_ingresada):
            salida += "|"
            salida += str(fila_ingresada[i])

        else:
            salida += "|"
            salida += str(fila_ingresada[i])
            
    salida += "|"  

    return salida


def imprimir_matriz(matriz_ingresada):
    # proposito: imprime una lista de listas en formato visual de matriz.
    # parametro: matriz/matriz ingresada/lista de listas.
    for fila in matriz_ingresada:
        print(imprimir_fila(fila))

#**************************************************************************************************** 


