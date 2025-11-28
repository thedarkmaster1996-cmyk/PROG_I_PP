from base_de_datos import *
from cargas import *
from impresiones import *

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
    