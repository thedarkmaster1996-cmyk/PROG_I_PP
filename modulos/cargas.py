import validaciones

def ingresar_en_indice(lista_ingresada, elemento, indice):
    """
    proposito: modifica el elemento del indice dado por el elemento dado en la lista dada.
    parametros: lista_ingresada/lista a modificar
                elemento/elemento por el que se reemplaza el elemento con el indice dado
                indice/indice del elemento
    """
    for i in range(len(lista_ingresada)):
        if i == indice:
            lista_ingresada[i] = elemento



def cargar_genero_de_estudiante(lista_gen,ind):
    """
    proposito: ingresa el genero de un estudiante en la lista "genero"
    parametros: lista_gen/ lista de generos m,f,x ingresada
                ind/ indice del estudiante
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





def cargar_apellido_nombre_estudiante(list_noms,ind_alumn):

    """
    proposito: ingresar el apellido y el nombre de un estudiante en el indice dado de la lista de estudiantes dada.
    parametros: list_noms/ lista de nombres de estudiantes
                ind_alumn/ indice donde se va cargar el apellido y nombre del alumno
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






def cargar_notas_de_alumno(indice_alumno,l_matriz,l_alumnos):

      
    for i in range(len(l_matriz[indice_alumno])):
       
        
        l_matriz[indice_alumno][i] = ingresar_nota(i,l_alumnos,indice_alumno)







def ingresar_nota(indice_materia,list_alumnos,ind_alumno): # validada
    """
    proposito : solicita y valida una nota comprendida entre 1 y 10 inclusive
    validacion: una vez ingresado un dato validado correctamente retorna la nota de no ser asi solicita la una nota nuevamente.
    
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




def cargar_legajo(lista_de_legajos,indice):
    """
    propopito: ingresa legajo de alumno validado a lista de legajos en el indice dado
    parametros: lista_de_legajos/ lista dada de legajos
                indice/ indice dado de la lista
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





