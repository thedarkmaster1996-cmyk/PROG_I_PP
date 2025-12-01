from base_de_datos import *
from validaciones import *
from ordenamiento import *
from impresiones import *

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


#        usar para buscar por legajo

def primer_indice(lista, elemento):
    salida = None
    for i in range(len(lista)):
        if lista[i] == elemento:
            salida = i
    return salida


###########################

def buscar_alumno_por_promedio(legajo_list: list, nombre_list: list, genero_list: list, calificaciones_mtz: list, promedios_list) -> None:
    
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
    




##########################


def promedio_materias(matriz_notas):
   
    proms_materias = [0,0,0,0,0]
    
    for i in range(0,5,1):
        proms_materias[i]= promedio_de_materia_en_matriz_de_notas(matriz_notas,i)

    
    proms_materias2 = copiar_lista(proms_materias)

    proms_materias2 = ordenamiento_asc_o_des_nums(proms_materias2,2)

    indice_materia = primer_indice(proms_materias, proms_materias2[0])

    print(f"promedio de materia mas alto : materia_{indice_materia + 1} promedio : {proms_materias2[0]:.1f}")
   
    """
    

 
    """






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

    
        


