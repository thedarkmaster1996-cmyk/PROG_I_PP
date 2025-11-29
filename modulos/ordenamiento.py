from validaciones import *
from base_de_datos import *
from calculos import *

def ordenamiento_burbuja_list(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0,n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista



def ordenamiento_asc_o_des_nums(l_ordenar,selec):

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





#                                             opcion 4 del menu 

#cambiar nombre a clonar lista
# copia una lista y trabaja con copias no cambia los valores de las originales

def copiar_lista(lista:list) -> list:
    """
    Copia una lista por valor.

    Args:
        lista (list): Lista a copiar.

    Returns:
        list: Lista copiada por valor. 
    """
    lista_nueva = [0] * len(lista)
    for i in range(len(lista)):
        lista_nueva[i] = lista[i]
    
    return lista_nueva

#Para ordenar y mostrar estudiantes por promedio:
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
                   
                    #Swap de promedio
                    aux = nuevo_promedios[j] 
                    nuevo_promedios[j] = nuevo_promedios[j+1]
                    nuevo_promedios[j+1] = aux

                    #Swap de legajo
                    aux = nuevo_legajos[j] 
                    nuevo_legajos[j] = nuevo_legajos[j+1]
                    nuevo_legajos[j+1] = aux

                    #Swap de nombre
                    aux = nuevo_nombres[j]
                    nuevo_nombres[j] = nuevo_nombres[j+1]
                    nuevo_nombres[j+1] = aux

                    #Swap de género
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






