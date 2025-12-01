from base_de_datos import *
from cargas import *
from impresiones import *
from calculos import *
from ordenamiento import *





def opcion_1():
    """
        proposito: realiza la carga de datos de un estudiante en las listas y matriz correspondientes
    """

    if validaciones.buscar_indice_disponible(estado) != False:

        alumno_indice = validaciones.buscar_indice_disponible(estado)

        print(f"estado {alumno_indice + 1} disponible para carga de datos")

        cargar_apellido_nombre_estudiante(estudiantes_nombre,alumno_indice)

        cargar_genero_de_estudiante(estudiantes_genero,alumno_indice)

        cargar_legajo(estudiantes_legajo,alumno_indice)

        cargar_notas_de_alumno(alumno_indice,matriz_de_calificaciones,estudiantes_nombre)

        estado[alumno_indice] = 1


    else:
        imprimir_en_pantalla("\t\t--no se encuentran estados disponibles --")



def opcion_2():
    """
        proposito: muestra todos los datos cargados en el sistema
    """

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
    """
        proposito: calcula y muestra el promedio de los estudiantes
    """

    calcular_promedio_alumnos(estado,matriz_de_calificaciones,estudiantes_promedio)

    imprimir_lista(estudiantes_promedio,"PROMEDIOS",estado)



def opcion_4():
    """
        proposito: ordena y muestra los datos de los estudiantes por promedio asc/desc
    """

    ordenar_promedios(matriz_de_calificaciones , estado, estudiantes_legajo, estudiantes_nombre, estudiantes_genero, estudiantes_promedio)
   


def opcion_5():
    """
        proposito: muestra la materia con mayor promedio general
    """
    promedio_materias(matriz_de_calificaciones)



def opcion_6():
    """
        proposito: buscar un alumno por su legajo e imprimir todos sus datos
    """

    calcular_promedio_alumnos(estado,matriz_de_calificaciones,estudiantes_promedio)

    imprimir_lista(estudiantes_legajo,"LEGAJOS",estado)

    buscar_alumno_por_legajo(estudiantes_legajo, estudiantes_nombre, estudiantes_genero, matriz_de_calificaciones, estudiantes_promedio)



def opcion_7():
    """
        proposito: mostrar cuantas veces se repite cada calificación en una materia dada
    """
    mostar_notas_por_materia(matriz_de_calificaciones)



mensaje_menu = "\t\tBIENVENIDO A GESTION DE ALUMNOS\nOpciones :\n1 - Realizar la carga de los datos\n2 - Mostrar todos los datos\n3 - Calcular el promedio de los estudiante\n4 - Ordenar y mostrar los datos de los estudiantes asc/des\n5 - Mostrar la materia con mayor promedio general\n6 - mostrar todos los datos por legajo\n7 - mostrar las veces se repiten calificaciónes en una asignatura\n8 - salir"



def sin_datos_cargados(li_estados:list) -> bool:
    """
    proposito: verifica si hay datos cargados en el sistema
    args:  
        li_estados : lista de estados
    """
    salida = True

    for i in range(len(li_estados)):
        if li_estados[i] == 1:
            salida = False
            break

    return salida 



def menu():


    while True:
        
        opcion = 0
        while True:

            if sin_datos_cargados(estado):
                print("\t\t--ADVERTENCIA: NO HAY DATOS CARGADOS EN EL SISTEMA--\npara contrinuar, por favor cargue\n")
                opcion_1()
            
            print(mensaje_menu)
            seleccion = input("Ingrese una opcion (1-8)\n: ")
            if es_entero(seleccion):
                opcion = int(seleccion)
                if opcion >=1 and opcion <=8:
                    break



        match opcion:
            case 1:
                print("\nCARGA DE DATOS: \n")
                opcion_1()

            case 2:
                print("\n MOSTRAR DATOS CARGADOS: \n")
                opcion_2()

            case 3:
                print("\n VER PROMEDIO POR ESTUDIANTE: \n")
                opcion_3()

            case 4:
                print("\n ORDENAR Y MOSTRAR ESTUDIANTES POR PROMEDIO: \n")
                opcion_4()

            case 5:
                print("\n MOSTRAR LA/S MATERIA/S CON MAYOR PROMEDIO GENERAL: \n")
                opcion_5()

            case 6:
                print("\n BUSCAR ESTUDIANTE POR LEGAJO: \n")
                opcion_6()

            case 7:
                print("\n BUSCAR Y MOSTRAR CUANTAS VECES SE REPITE CADA CALIFICACIÓN: \n")
                opcion_7()

            case 8:
                print("**HASTA PRONTO!!")
                break



menu()