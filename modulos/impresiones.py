def imprimir_en_pantalla(dato_ingresado):
    """
    proposito: imprime el dato dado
    parametro: dato_ingresado/ dato a imprimir en pantalla
    """
    print(dato_ingresado)




def imprimir_notas_por_materia(matriz_de_nots,ind):
    for i in range(len(matriz_de_nots[ind])):
        imprimir_en_pantalla(f"Materia_{i + 1} : {matriz_de_nots[ind][i]}")



def mostrar_datos_alumno(indice_ing , list_legajos, list_alumnos, list_genero, matriz_de_notas):
    
    """
    proposito: muestra en pantalla todos los datos de un alumno segun su indice.
        (legajo,nombre,genero,notas)  # ******* falta agregar promedios **********
    parametro: indice_est/ indice del estudiante a mostrar datos
    """
    

    imprimir_en_pantalla(f"\tlegajo: {list_legajos[indice_ing]}")
    imprimir_en_pantalla(f"\tnombre completo: {list_alumnos[indice_ing]}")
    imprimir_en_pantalla(f"\tgenero del alumno: {list_genero[indice_ing]}")
    imprimir_en_pantalla("\t-NOTAS-")
    imprimir_notas_por_materia(matriz_de_notas,indice_ing)




def imprimir_alumno_con_indice(indice_est,l_legajo,l_alumnos,l_genero,l_matriz_notas):
    """
    proposito: muestra en pantalla todos los datos de un alumno segun su indice.
    (legajo,nombre,genero,notas)  # ******* falta agregar promedios **********
    parametro: indice_est/ indice del estudiante a mostrar datos
    """
    mostrar_datos_alumno(indice_est,l_legajo,l_alumnos,l_genero,l_matriz_notas)




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



