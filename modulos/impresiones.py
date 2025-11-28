def imprimir_en_pantalla(dato_ingresado):
    """
    proposito: imprime el dato dado
    parametro: dato_ingresado/ dato a imprimir en pantalla
    """
    print(dato_ingresado)


####################################
#             en revision

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

#######################


def preparar_fila(fila_ingresada):
# proposito: imprime una lista como fila visual de matriz.
# parametro: fila_ingresada/ fila a imprimir en formato matriz.
    salida = ""

    for i in range(len(fila_ingresada)):
        if i == 0:
            salida += "|   "
            salida += str(fila_ingresada[i])
           
        elif i == len(fila_ingresada):
            salida += str(fila_ingresada[i])
            salida += "    |"

        else:
            salida += "   "
            salida += str(fila_ingresada[i])
            
    salida += "   |"  

    return salida


def imprimir_matriz(matriz_ingresada):
    # proposito: imprime una lista de listas en formato visual de matriz.
    # parametro: matriz/matriz ingresada/lista de listas.
    for fila in matriz_ingresada:
        print(preparar_fila(fila))






def imprimir_lista(lista_ingresada: list, nombre_de_lista : str, lista_estado: list) -> None:
# proposito: imprime una lista 
# parametro: lista_ingresada/ lista a imprimir 
    salida = ""

    for i in range(len(lista_estado)):
        if lista_estado[i] == 1:
            if i == 0:
                salida += "| "
                salida += str(lista_ingresada[i])
            
            elif i == len(lista_ingresada):
                salida += str(lista_ingresada[i])
                salida += " "

            else:
                salida += " * "
                salida += str(lista_ingresada[i])
        else:
            continue
            
    salida += " | "  
    salida += nombre_de_lista

    print(salida) 







def imprimir_todos_los_datos_cargados(matriz_De_notas, legajo_estudiantes, nombre_estudiantes: list, genero_estudiantes: list, estudiante_estado:list) -> None:
    """
    Función que imprime lo que se encuentra cargado en la matriz y arrays compartidos.

    Args:
            calificaciones (list): Matriz con calificaciones.
            legajo_estudiante (list): Array con número de legajo de estudiantes. 
            nombre_estudiante (list): Array con nombres de estudiantes.
            genero_estudiante (list): Array con géneros correspondientes a los estudiantes. 
        """
    
    for i in range(len(matriz_De_notas)):
        if estudiante_estado[i] == 1:



            print(f"alumno")



            print(f"\tLegajo\n: {legajo_estudiantes[i]}\n")
            print(f"\tNombre y apellido\n: {nombre_estudiantes[i]}\n")
            print(f"\tGénero\n: {genero_estudiantes[i]}\n")

            for j in range(len(matriz_De_notas[i])): 
                print(f"\tMateria_{j+1}\nnota: {matriz_De_notas[i][j]}\n")




















def mostrar_lista_numeros(lista_numeros, margen=20):
    """
    Muestra de manera estética los elementos de una lista numérica.
    
    Args:
        lista_numeros (list): Lista de números a mostrar
        margen (int): Espacio adicional para márgenes (default: 6)
    """
    if not lista_numeros:
        print("Lista vacía")
        return
    
    # Calcular dimensiones para formato dinámico
    ancho_numero = 0
    ancho_indice = len(str(len(lista_numeros)))
    
    # Calcular ancho del número más largo manualmente
    for numero in lista_numeros:
        longitud_actual = len(str(numero))
        if longitud_actual > ancho_numero:
            ancho_numero = longitud_actual
    
    # Aplicar márgenes personalizables
    ancho_columna_indice = ancho_indice + margen
    ancho_columna_valor = ancho_numero + margen
    
    # Encabezado con márgenes amplios
    print("┌" + "─" * (ancho_columna_indice + 2) + "┬" + "─" * (ancho_columna_valor + 2) + "┐")
    print(f"│ {'ÍNDICE':^{ancho_columna_indice}} │ {'VALOR':^{ancho_columna_valor}} │")
    print("├" + "─" * (ancho_columna_indice + 2) + "┼" + "─" * (ancho_columna_valor + 2) + "┤")
    
    # Elementos de la lista con espacio amplio
    for indice, numero in enumerate(lista_numeros):
        print(f"│ {indice + 1:>{ancho_columna_indice}} │ {numero:>{ancho_columna_valor}} │")
    
    # Pie de tabla
    print("└" + "─" * (ancho_columna_indice + 2) + "┴" + "─" * (ancho_columna_valor + 2) + "┘")

    