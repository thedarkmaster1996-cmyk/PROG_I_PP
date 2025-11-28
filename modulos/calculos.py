def sumar_fila_numeros(lista):
    acumulador = 0
    for numero in lista:
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

def promedio_alumno(matriz_de_notas,indice_de_alumno):
    promedio = sumar_fila_numeros(matriz_de_notas[indice_de_alumno]) / len(matriz_de_notas[indice_de_alumno])

    return promedio





