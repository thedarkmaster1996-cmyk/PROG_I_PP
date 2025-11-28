from base_de_datos import *
from cargas import *
from impresiones import *
from calculos import *
from ordenamiento import *





def opcion_1():

    if validaciones.buscar_indice_disponible(estado) != False:

        alumno_indice = validaciones.buscar_indice_disponible(estado)

        print(alumno_indice)

        cargar_apellido_nombre_estudiante(estudiantes_nombre,alumno_indice)

        cargar_genero_de_estudiante(estudiantes_genero,alumno_indice)

        cargar_legajo(estudiantes_legajo,alumno_indice)

        estado[alumno_indice] = 1


    else:
        imprimir_en_pantalla("\t\t--no se encuentran estados disponibles --")



def opcion_2():

    # esta mal, pide mostrar todo ++ necesito una funcion que imprima prolijo listas

    print("\t\tMATRIZ DE NOTAS")
    imprimir_matriz(matriz_de_calificaciones)
    print("  ")

    imprimir_lista(estudiantes_nombre,"ESTUDIANTES",estado)
    print("  ")

    imprimir_lista(estudiantes_legajo,"LEGAJOS",estado)
    print("  ")

    imprimir_lista(estudiantes_genero,"GENERO",estado)
    print("  ")

    imprimir_lista(estudiantes_promedio,"PROMEDIOS",estado)


def opcion_3():

    calcular_promedio_alumnos(estado,matriz_de_calificaciones,estudiantes_promedio)

    imprimir_lista(estudiantes_promedio,"PROMEDIOS",estado)



def opcion_4():

    ordenar_promedios(matriz_de_calificaciones , estado, estudiantes_legajo, estudiantes_nombre, estudiantes_genero, estudiantes_promedio)
   

def opcion_5():
    pass