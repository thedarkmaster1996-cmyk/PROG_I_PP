from base_de_datos import *
from validaciones import *

def sumar_fila_numeros(lista_de_numeros) -> int:
    
    acumulador = 0
    for numero in lista_de_numeros:
        acumulador += numero
    return acumulador




#promedioa las calificaciones de una materia dada por el indice

def promedio_de_materia_en_matriz_de_notas(matriz_ingresada,indice_de_la_materia):

    acumulador = 0

    for fila in matriz_ingresada:
        acumulador += fila[indice_de_la_materia]
    salida = acumulador / len(matriz_ingresada)

    return salida


# promedio de notas de un alumno por su indice   retorna el promedio




# Ejemplo de uso
#mi_lista = [1, 2, 3]
#nueva_lista = append_cacero(mi_lista, 4)
#print(nueva_lista)  # [1, 2, 3, 4]


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

    
        



