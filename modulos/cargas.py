import validaciones


def ingresar_en_indice(lista_ingresada:list, elemento:None, indice:int) -> None:
    """
    proposito: ingresa un elemento en la lista dada en el indice dado

    Args:
        lista_ingresada : lista donde se ingresara el elemento
        elemento : elemento a ingresar
        indice : indice donde se ingresara el elemento
    """
    for i in range(len(lista_ingresada)):
        if i == indice:
            lista_ingresada[i] = elemento



def cargar_genero_de_estudiante(lista_gen:list, ind:int) -> None:
    """
    proposito: cargar el genero de un estudiante en la lista de generos dada en el indice dado

    Args:
        lista_gen : lista de generos donde se cargara el genero
        ind : indice donde se cargara el genero
    """

    while True:
        seleccion = input("\t\tseleccione un genero:\n 1 : M\n 2 : F\n 3 : X\n :")
        
        
        match seleccion:
            case "1": 
                lista_gen[ind] = "M"
            case "2": 
                lista_gen[ind] = "F"
            case "3":
                lista_gen[ind] = "X"
            case _:
                print("\t\t-opcion invalida-")
        
        if seleccion == "1" or seleccion == "2" or seleccion == "3":
            break



def cargar_apellido_nombre_estudiante(list_noms:list, ind_alumn:int) -> None:

    """
    proposito: cargar el apellido y nombre de un estudiante en la lista de nombres dada en el indice dado
    Args:
        list_noms : lista de nombres donde se cargara el nombre
        ind_alumn : indice donde se cargara el nombre
    """
    apellido_validado = ""
    nombre_validado = ""
    while True:
        
        while True:
            apellido = input("\t\tdigite el apellido del del estudiante\n :")
            if validaciones.solo_cadena(apellido) == True:
                apellido_validado = validaciones.pasar_a_minuscula(apellido)
                break
            else: print("\t\tapellido invalido vuelva a intentarlo")

        while True:
            nombre = input("\t\tdigite el nombre del estudiante\n :")
            if validaciones.solo_cadena(nombre) == True:
                nombre_validado = validaciones.pasar_a_minuscula(nombre)
                break
            else: print("\t\tnombre invalido vuelva a intentarlo")
        break

    nombre_completo = apellido_validado + " " + nombre_validado
    list_noms[ind_alumn] = nombre_completo



def cargar_notas_de_alumno(indice_alumno:int, l_matriz:list ,l_alumnos:list) -> None:
    """
    proposito: cargar las notas de un alumno en la matriz de calificaciones dada en el indice dado

    Args:
        indice_alumno : indice del alumno a cargar notas
        l_matriz : lista de listas con las calificaciones
        l_alumnos : lista de nombres de alumnos
    """

      
    for i in range(len(l_matriz[indice_alumno])):
       
        
        l_matriz[indice_alumno][i] = ingresar_nota(i,l_alumnos,indice_alumno)



def ingresar_nota(indice_materia:int, list_alumnos:list, ind_alumno:int) -> int:
    """
    proposito: ingresa una nota validada para un alumno en una materia dada

    Args:
        indice_materia : indice de la materia
        list_alumnos : lista de alumnos
        ind_alumno : indice del alumno

    Returns:
        int: nota validada
    """
    alumno = list_alumnos[ind_alumno]
    while True:


        nota_ingreso = input(f"\t\t{alumno}\n\tMateria_{indice_materia + 1}\t\tdigite la nota del estudiante que este entre 1 y 10 \n\t: ")
        #
        if  validaciones.es_entero(nota_ingreso) == True:

            nota = int(nota_ingreso)
            if validaciones.numero_entre_1_y_10(nota) == True:
        
                salida = nota
                break
            else: print("\t\t-nota fuera del rango de 1 a 10-")

        else: print("\t\t-digito invalido-")
        
    return salida



def cargar_legajo(lista_de_legajos:list, indice:int) -> None:
    """
    proposito: cargar el legajo de un estudiante en la lista de legajos dada en el indice dado
    Args:
        lista_de_legajos : lista de legajos donde se cargara el legajo
        indice : indice donde se cargara el legajo
    """
    
    while True:
      
        numero = input("\tingrese el legajo del alumno\n\tnumero entero de seis cifras positivo\n\t:")
        if len(numero) == 6 and validaciones.es_entero(numero) == True and ord(numero[0]) != 45 :
            valor = int(numero)
            if validaciones.esta_en_lista(valor,lista_de_legajos) == False:
            
                lista_de_legajos[indice] = valor #modifique ctrol z si quiero volver
                break
            else:print("\t\t-legajo existente-")
        else: print("\t\t-legajo invalido-\nintentelo nuevamente: ")





