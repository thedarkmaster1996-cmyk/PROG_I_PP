from base_de_datos import *
from validaciones import *
from ordenamiento import *
from impresiones import *


def sumar_fila_numeros(lista_de_numeros:list) -> int:
    """
    proposito: suma los elementos de una lista de numeros y retorna la suma
    Args:
        lista_de_numeros : lista de elementos de tipo numérico

    Returns:
        acumulador : suma de los elementos de la lista y retorna la suma
    """
    
    acumulador = 0
    for numero in lista_de_numeros:
        acumulador += numero
    return acumulador



def promedio_de_materia_en_matriz_de_notas(matriz_ingresada:list ,indice_de_la_materia:int) -> float:
    """
    proposito: calcula el promedio de una materia dada por su indice en una matriz de notas

    Args:
        matriz_ingresada : lista de listas con las calificaciones
        indice_de_la_materia : indice de la materia a promediar

    Returns:
        float: promedio de la materia
    """
    acumulador = 0
    for fila in matriz_ingresada:
        acumulador += fila[indice_de_la_materia]
    return acumulador / len(matriz_ingresada)
    #print(acumulador / len(matriz_ingresada))



def primer_indice(lista:list, elemento:None) -> int:
    """
    proposito: busca el primer indice de un elemento en una lista

    Args:
        lista : lista donde se buscara el elemento
        elemento : elemento a buscar

    Returns:
        int: indice del primer elemento encontrado
    """
    salida = None
    for i in range(len(lista)):
        if lista[i] == elemento:
            salida = i
    return salida



def buscar_alumno_por_legajo(legajo_list: list, nombre_list: list, genero_list: list, calificaciones_mtz: list, promedios_list) -> None:
    """
    proposito: busca y muestra un alumno por su legajo
    Args:
        legajo_list : lista de legajos
        nombre_list : lista de nombres
        genero_list : _lista de generos
        calificaciones_mtz :  lista de listas de calificaciones
        promedios_list : _lista de promedios
    """
    
    existe_legajo = 0
    while True:
        
        legajo_ingresado = input("\t\tIngrese el legajo que desea buscar\n: ")

        while solo_numeros(legajo_ingresado) == False or len(legajo_ingresado) != 6:
            
            legajo_ingresado = input("\t\tlegajo inexistente.\nIngrese el legajo que desea buscar\n: ")
            validar_int = solo_numeros(legajo_ingresado)

        for i in range(len(legajo_list)):

            if int(legajo_ingresado) == legajo_list[i]:

                print(f"\nlejago: {legajo_list[i]} alumno: {nombre_list[i]} genero: {genero_list[i]} promedio : {promedios_list[i]}")
            

                for j in range(len(calificaciones_mtz[i])): 
                    print(f"Nota Materia_{j+1}: {calificaciones_mtz[i][j]}")
                existe_legajo = 1
                break
            else:
                continue
        if existe_legajo == 0:
            print("\t   legajo inexistente")
            
        # preguntar si quiere ver otro alumno
        selleccion = input("\tquiere buscar otro alumno?\n-s- para si / cualquier tecla para volver al menu\n:")
        if pasar_a_minuscula(selleccion) != "s":
            break
    


def promedio_materias(matriz_notas:list) -> None:
    """
    proposito: muestra la materia con el promedio mas alto
    Args:
        matriz_notas : lista de listas con las calificaciones
    """
   
    proms_materias = [0,0,0,0,0]
    
    for i in range(0,5,1):
        proms_materias[i]= promedio_de_materia_en_matriz_de_notas(matriz_notas,i)

    
    proms_materias2 = copiar_lista(proms_materias)

    proms_materias2 = ordenamiento_asc_o_des_nums(proms_materias2,2)

    indice_materia = primer_indice(proms_materias, proms_materias2[0])

    print(f"promedio de materia mas alto : materia_{indice_materia + 1} promedio : {proms_materias2[0]:.1f}")
   
    
    
def promedio_alumno(matriz_de_notas:list,indice_de_alumno:int) -> float:
    """
    proposito: calcula el promedio de un alumno dado por su indice en una matriz de notas
    Args:
        matriz_de_notas : lista de listas con las calificaciones
        indice_de_alumno : indice del alumno a promediar

    Returns:
        float: promedio del alumno
    """
    promedio = sumar_fila_numeros(matriz_de_notas[indice_de_alumno]) / len(matriz_de_notas[indice_de_alumno])

    return promedio



def calcular_promedio_alumnos(estados_lista:list, notas_matriz:list, promedio_estudiantes:list) -> None:
    """
    proposito: calcula el promedio de todos los alumnos y los guarda en la lista de promedios
    Args:
        estados_lista : lista de estados
        notas_matriz : lista de listas con las calificaciones
        promedio_estudiantes : lista de promedios
    """
   
    for i in range(len(estados_lista)):
        if estados_lista[i] != 0 :
            promedio_estudiantes[i] = promedio_alumno(notas_matriz,i)
    

        
def imprimir_promedio_alumnos(estados_lista:list, notas_matriz:list, promedio_estudiantes:list, nombres_estudiantes:list, legajo_estudiante:list) -> None:
    """
    proposito: imprime el promedio de todos los alumnos con sus datos
    Args:
        estados_lista : lista de estados
        notas_matriz : lista de listas con las calificaciones
        promedio_estudiantes : lista de promedios
        nombres_estudiantes : lista de nombres
        legajo_estudiante : lista de legajos
    """
   
    for i in range(len(estados_lista)):
        if estados_lista[i] != 0:

            print(f"*alumno: {nombres_estudiantes[i]}  * legajo: {legajo_estudiante[i]}  * promedio: {promedio_estudiantes[i]}\n")

    
        


