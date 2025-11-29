from base_de_datos import *
from validaciones import *
from ordenamiento import *

def sumar_fila_numeros(lista_de_numeros) -> int:
    
    acumulador = 0
    for numero in lista_de_numeros:
        acumulador += numero
    return acumulador



#######################




#promedioa las calificaciones de una materia dada por el indice

def promedio_de_materia_en_matriz_de_notas(matriz_ingresada,indice_de_la_materia):
    acumulador = 0
    for fila in matriz_ingresada:
        acumulador += fila[indice_de_la_materia]
    return acumulador / len(matriz_ingresada)
    #print(acumulador / len(matriz_ingresada))



# promedio de notas de un alumno por su indice   retorna el promedio




def primer_indice(lista, elemento):
    salida = None
    for i in range(len(lista)):
        if lista[i] == elemento:
            salida = i
    return salida


def promedio_materias(matriz_notas):
   
    proms_materias = [0,0,0,0,0]
    
    for i in range(0,5,1):
        proms_materias[i]= promedio_de_materia_en_matriz_de_notas(matriz_notas,i)

    
    proms_materias2 = copiar_lista(proms_materias)

    proms_materias2 = ordenamiento_asc_o_des_nums(proms_materias2,2)

    indice_materia = primer_indice(proms_materias, proms_materias2[0])

    print(f"promedio de materia mas alto : materia_{indice_materia + 1} promedio : {proms_materias2[0]:.1f}")
   







#######################
def promedio_alumno(matriz_de_notas,indice_de_alumno):
    promedio = sumar_fila_numeros(matriz_de_notas[indice_de_alumno]) / len(matriz_de_notas[indice_de_alumno])

    return promedio







def calcular_promedio_alumnos(estados_lista, notas_matriz, promedio_estudiantes):
   
    for i in range(len(estados_lista)):
        if estados_lista[i] != 0 :
            promedio_estudiantes[i] = promedio_alumno(notas_matriz,i)
    




        
def imprimir_promedio_alumnos(estados_lista, notas_matriz, promedio_estudiantes, nombres_estudiantes, legajo_estudiante):
   
    for i in range(len(estados_lista)):
        if estados_lista[i] != 0:

            print(f"*alumno: {nombres_estudiantes[i]}  * legajo: {legajo_estudiante[i]}  * promedio: {promedio_estudiantes[i]}\n")

    
        


