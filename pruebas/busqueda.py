


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

