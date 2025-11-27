import modulos as modulo
import generadores as gen

modulo.imprimir_matriz(gen.generar_matriz_nula(5,5))
cant = 3

estados = gen.generar_lista_de_elementos(cant,0)

estudiantes = gen.generar_lista_de_elementos(cant,"")

legajos = gen.generar_lista_de_elementos(cant,000000)

genero = gen.generar_lista_de_elementos(cant,"")

notas = gen.generar_matriz_nula(cant,5)

def cargar_datos_de_estudiante(indice):
    while True:
        val1 = modulo.buscar_indice_disponible(estados)
        if val1 != False:
            estados[val1] = 1
            cargar_legajo()

        



