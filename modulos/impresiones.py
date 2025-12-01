from validaciones import *
from base_de_datos import * 


def imprimir_en_pantalla(dato_ingresado:None) -> None:
    """
    proposito: imprime en pantalla el dato ingresado

    Args:
        dato_ingresado : dato a imprimir
    """
    print(dato_ingresado)



def mostar_notas_por_materia(matriz_cals:list) -> None:
    """
    proposito: muestra la cantidad de notas numericas iguales en una materia especifica

    Args:
        matriz_cals : lista de listas con las calificaciones
    """
    numero = 0
    while True: 

        num_seleccionado = input("\tver cantidad individual de notas numericas iguales en una materia especifica\n\tmaterias disponibles: | 1 - 2 - 3 - 4 - 5 | ")


        if es_entero(num_seleccionado) and valor_de_1_a_5(num_seleccionado):
            numero = int(num_seleccionado)
            break
        else: 
            print("\tmateria inexistente")
            print("\tmaterias disponibles: | 1 - 2 - 3 - 4 - 5 |")
 
    

    for i in range(len(matriz_cals)):

        nota = matriz_cals[i][numero - 1]

        if nota >= 1 and nota <= 10:
            cantidad_notas_individuales[nota - 1] += 1
    

    
    print(f"Materia_{numero}: ")
    print("  ")

    for j in range(len(cantidad_notas_individuales)):

        print(f"veces que se repite la nota {j+1} : {cantidad_notas_individuales[j]}")



def imprimir_notas_por_materia(matriz_de_nots:list ,ind:int) -> None:
    """
    proposito: imprime en pantalla las notas de un alumno por su indice
    Args:
        matriz_de_nots : lista de listas con las calificaciones
        ind : indice del alumno
    """

    for i in range(len(matriz_de_nots[ind])):
        imprimir_en_pantalla(f"Materia_{i + 1} : {matriz_de_nots[ind][i]}")



def mostrar_datos_alumno(indice_ing , list_legajos, list_alumnos, list_genero, matriz_de_notas) -> None:
   
    """
    proposito: muestra en pantalla todos los datos de un alumno segun su indice.
    args:
        indice_ing : indice del alumno a mostrar datos
        list_legajos : lista de legajos
        list_alumnos : lista de nombres
        list_genero : lista de generos
        matriz_de_notas : lista de listas con las calificaciones
    """
    

    imprimir_en_pantalla(f"\tlegajo: {list_legajos[indice_ing]}")
    imprimir_en_pantalla(f"\tnombre completo: {list_alumnos[indice_ing]}")
    imprimir_en_pantalla(f"\tgenero del alumno: {list_genero[indice_ing]}")
    imprimir_en_pantalla("\t-NOTAS-")
    imprimir_notas_por_materia(matriz_de_notas,indice_ing)



def imprimir_alumno_con_indice(indice_est:list ,l_legajo:list ,l_alumnos:list ,l_genero:list ,l_matriz_notas:list) -> None:
    """
    proposito: imprime en pantalla todos los datos de un alumno segun su indice

    Args:
        indice_est : indice del alumno a mostrar datos
        l_legajo : lista de legajos
        l_alumnos : lista de nombres
        l_genero : lista de generos
        l_matriz_notas : lista de listas con las calificaciones
    """
    mostrar_datos_alumno(indice_est,l_legajo,l_alumnos,l_genero,l_matriz_notas)



def preparar_fila(fila_ingresada:list) -> str:
    """
    proposito: prepara una fila para ser impresa en formato visual de matriz
    Args:
        fila_ingresada : fila a preparar esteticamente

    Returns:
        str: fila preparada para imprimir
    """
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



def imprimir_matriz(matriz_ingresada:list) -> None:
    """
    proposito: imprime en pantalla una matriz en formato visual
    Args:
        matriz_ingresada : lista de listas a imprimir
    """
    for fila in matriz_ingresada:
        print(preparar_fila(fila))



def imprimir_lista(lista_ingresada:list, nombre_de_lista :str, lista_estado:list) -> None:
    """
    proposito: imprime en pantalla una lista en formato visual
    Args:
        lista_ingresada : lista a imprimir
        nombre_de_lista: nombre de la lista a imprimir
        lista_estado : lista de estados para filtrar elementos activos
    """
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



def imprimir_todos_los_datos_cargados(matriz_De_notas:list, legajo_estudiantes:list, nombre_estudiantes:list, genero_estudiantes:list, estudiante_estado:list) -> None:
    """
    Función que imprime lo que se encuentra cargado en la matriz y arrays compartidos

    Args:
            calificaciones : lista de listas con las calificaciones
            legajo_estudiante : lista con legajos de estudiantes
            nombre_estudiante : lista con nombres de estudiantes   
            genero_estudiante : lista con generos de estudiantes
            estudiante_estado : lista con estados de estudiantes


        """
    
    for i in range(len(matriz_De_notas)):
        if estudiante_estado[i] == 1:



            print(f"alumno")



            print(f"\tLegajo\n: {legajo_estudiantes[i]}\n")
            print(f"\tNombre y apellido\n: {nombre_estudiantes[i]}\n")
            print(f"\tGénero\n: {genero_estudiantes[i]}\n")

            for j in range(len(matriz_De_notas[i])): 
                print(f"\tMateria_{j+1}\nnota: {matriz_De_notas[i][j]}\n")













