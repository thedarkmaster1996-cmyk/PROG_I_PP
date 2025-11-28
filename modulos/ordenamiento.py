
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



