

#funciona

#import modulos as modulo






#genera una lista de elementos
def generar_lista_de_elementos(n,e):
    """
    proposito: genera una lista de "n" elementos y de elemento default "e"
    parametro: e/elementos default de la lista
               n/numero de elementos de la lista
    """

    salida = [e] * n
    return salida


#genera una matriz nula de solo ceros

def generar_matriz_nula(f,c):
    """
        proposito: genera una matriz de "n" filas x "m" columnas con "e" como elemento por default
        parametros: f/filas de la matriz
                    c/columnas de la matriz
                    e/elemento por default
    """
    matriz = generar_lista_de_elementos(f,[])

    for i in range(len(matriz)):
        matriz[i] = generar_lista_de_elementos(c,0)
    return matriz




# prueba git
