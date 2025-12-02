from validaciones import *
from base_de_datos import *


def ordenamiento_burbuja_list(lista:list) -> list:
    """
    proposito: ordena una lista de numeros de forma ascendente usando el metodo burbuja
    Args:
        lista : lista de numeros a ordenar

    Returns:
        list: lista ordenada
    """
    n = len(lista)
    for i in range(n):
        for j in range(0,n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista




def ordenamiento_asc_o_des_nums(l_ordenar:list, selec:int) -> list:
    """
    proposito: ordena una lista de numeros de forma ascendente o descendente segun la seleccion del usuario
    Args:
        l_ordenar : lista de numeros a ordenar
        selec (_type_): seleccion de ordenamiento 1 asc 2 des

    Returns:
        list: lista ordenada
    """

    ingreso = selec
    salida = None
    if selec == 1:
        
        n = len(l_ordenar)
        for i in range(n):
            for j in range(0,n - i - 1):
                if l_ordenar[j] > l_ordenar[j + 1]:
                    l_ordenar[j], l_ordenar[j + 1] = l_ordenar[j + 1], l_ordenar[j]
        salida = l_ordenar
    elif selec == 2:

        n = len(l_ordenar)
        for i in range(n):
            for j in range(0,n - i - 1):
                if l_ordenar[j] < l_ordenar[j + 1]:
                    l_ordenar[j], l_ordenar[j + 1] = l_ordenar[j + 1], l_ordenar[j]
        salida = l_ordenar
    return salida



def copiar_lista(lista:list) -> list:
    
    """
    proposito: copia una lista y devuelve la copia
    Args:
        lista : lista a copiar
    Returns:
        list: lista copiada
    """
    lista_nueva = [0] * len(lista)
    for i in range(len(lista)):
        lista_nueva[i] = lista[i]
    
    return lista_nueva



def sumar_fila_numeros(lista_de_numeros:list) -> int:
    """_summary_
    proposito: suma los numeros de una lista y devuelve la suma
    Args:
        lista_de_numeros : lista de numeros a sumar

    Returns:
        int: suma de los numeros
    """
    acumulador = 0
    for numero in lista_de_numeros:
        acumulador += numero
    return acumulador



def promedio_alumno(matriz_de_notas:list, indice_de_alumno:int) -> float:
    """
    proposito: calcula el promedio de un alumno en la matriz de notas dada
    Args:
        matriz_de_notas : lista de listas con las calificaciones
        indice_de_alumno : indice del alumno a promediar

    Returns:
        float: promedio del alumno
    """
    promedio = sumar_fila_numeros(matriz_de_notas[indice_de_alumno]) / len(matriz_de_notas[indice_de_alumno])

    return promedio



def calcular_promedio_alumnos(estados_lista, notas_matriz, promedio_estudiantes) -> None:
    """
    proposito: calcula el promedio de todos los alumnos y lo guarda en la lista de promedios
    Args:
        estados_lista :  lista de estados
        notas_matriz :  lista de listas con las calificaciones
        promedio_estudiantes :  lista de promedios
    """
   
    for i in range(len(estados_lista)):
        if estados_lista[i] != 0 :
            promedio_estudiantes[i] = promedio_alumno(notas_matriz,i)



def ordenar_promedios(matriz_notas: list, lista_estados: list, legajo_estudiante: list, nombre_estudiante: list, genero_estudiante: list,promedios_alumnos: list) -> None:
    """
    La función ordena y muestra a los estudiantes por promedio. 

    Args:
        calificaciones (list): Array con notas de los estudiantes.
        estado_legajo (list): Array con el estado del legajo: 0 inactivo | 1 activo. Se utiliza para buscar encontrar datos de estudiantes.  
        legajo_estudiante (list): Array con número de legajo de estudiantes. 
        nombre_estudiante (list): Array con nombres de estudiantes.
        genero_estudiante (list): Array con géneros correspondientes a los estudiantes. 
    """
    # cambiar por mi funcion calcular promedio

    calcular_promedio_alumnos(lista_estados,matriz_notas,promedios_alumnos)
    
# copia las listas y trabaja con copias


    nuevo_promedios = copiar_lista(promedios_alumnos)
    nuevo_legajos = copiar_lista(legajo_estudiante)
    nuevo_nombres = copiar_lista(nombre_estudiante)
    nuevo_generos = copiar_lista(genero_estudiante)


#  seleccion del usuario


# valida la selleccion del usuario
    seleccion = ""
    while True:
        opcion = input("Desea mostrar de forma descendente? s|n\n:")

        print("  ") # agrego una separacion entre el titulo y el contenido


        if solo_cadena(opcion) == True and pasar_a_minuscula(opcion) == "s":
            seleccion = "s"
            break
        elif solo_cadena(opcion) == True and pasar_a_minuscula(opcion) == "n":
            seleccion = "n"
            break
        else:
            print("\topcion invalida")

       # cambiar por la funcion pasar a minuscula
        

    # forma decendente 


    cant = len(promedios_alumnos) 

    # s minuscula

    if seleccion == "s":

        for i in range(cant):
            for j in range(0,cant - i -1):
                if nuevo_promedios[j] < nuevo_promedios[j + 1]: 
                   
                   # lo mismo que el else pero al revez
                   
                    #promedio
                    aux = nuevo_promedios[j] 
                    nuevo_promedios[j] = nuevo_promedios[j+1]
                    nuevo_promedios[j+1] = aux

                    #legajo
                    aux = nuevo_legajos[j] 
                    nuevo_legajos[j] = nuevo_legajos[j+1]
                    nuevo_legajos[j+1] = aux

                    #nombre
                    aux = nuevo_nombres[j]
                    nuevo_nombres[j] = nuevo_nombres[j+1]
                    nuevo_nombres[j+1] = aux

                    #género
                    aux = nuevo_generos[j]
                    nuevo_generos[j] = nuevo_generos[j+1]
                    nuevo_generos[j+1] = aux
    
    elif seleccion == "n":

        # forma acendente 
        
        for i in range(cant):
            for j in range(0,cant - i -1):
                if nuevo_promedios[j] > nuevo_promedios[j + 1]: 
                    
                    # ordena las copias de las listas todas al mismo tiempo y las imprime
                    
                    # ordenado de promedio
                    aux = nuevo_promedios[j] 
                    nuevo_promedios[j] = nuevo_promedios[j+1]
                    nuevo_promedios[j+1] = aux

                    # ordenado de legajo
                    aux = nuevo_legajos[j] 
                    nuevo_legajos[j] = nuevo_legajos[j+1]
                    nuevo_legajos[j+1] = aux

                    # ordena de nombre
                    aux = nuevo_nombres[j]
                    nuevo_nombres[j] = nuevo_nombres[j+1]
                    nuevo_nombres[j+1] = aux

                    # ordena de género
                    aux = nuevo_generos[j]
                    nuevo_generos[j] = nuevo_generos[j+1]
                    nuevo_generos[j+1] = aux




    for i in range(len(promedios_alumnos)):
        if nuevo_legajos[i] != 0:

            print(f"*alumno: {nuevo_nombres[i]}  * legago: {nuevo_legajos[i]} * genero: {nuevo_generos[i]} * promedio: {nuevo_promedios[i]}\n")






