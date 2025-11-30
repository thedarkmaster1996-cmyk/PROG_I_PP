


def valor_de_1_a_5(valor_ingresado:str) -> bool:
    salida = False
    if ord(valor_ingresado) >= 49 and ord(valor_ingresado) <= 53:
        salida = True

    return salida





def buscar_indice_disponible(lista_estados):
#proposito : devuelve el indice disponible de una lista.
        #  *EN CASO DE NO HABER INDICE DISPONIBLE RETORNA FALSE*
#parametro : lista_estados/lista ingresada de estados

    contador = 0
    resultado = None
    for i in range(len(lista_estados)):        
        if lista_estados[i] == 0 and contador == 0:
            contador +=1
            resultado = i
    if contador == 0:
        resultado = False
    return resultado




def pasar_a_minuscula(texto_ingresado :str):
    """
    proposito : pasar todos los caracteres de una cadena a minusculas
    """

    salida = ""

    for caracter in range(len(texto_ingresado)):
        if ord(texto_ingresado[caracter]) >= 65 and ord(texto_ingresado[caracter]) <= 90:
            letra_minuscula = chr(ord(texto_ingresado[caracter]) + 32)
            salida += letra_minuscula
        
        else:
            salida += texto_ingresado[caracter]
            
        if ord(texto_ingresado[caracter]) == 165:
            letra_minuscula = chr(ord(texto_ingresado[caracter]) - 1)
            salida += letra_minuscula
        
    return salida


def solo_cadena(dato_a_evaluar:str):

    """
    proposito: determina si todos los caracteres representan un numero
    """

    salida = True
    ingreso = pasar_a_minuscula(dato_a_evaluar)
    for digito in ingreso:
        if ord(digito) > 122 or ord(digito) < 97:
            salida = False

    
    return salida


def solo_numeros(dato_a_evaluar:str):

    """
    proposito: determina si todos los caracteres representan un numero
    """
    salida = True
    for digito in dato_a_evaluar:
        if ord(digito) > 57 or ord(digito) < 48:
            salida = False

    return salida


def validar_si_es_10(nota_ingresada:str):
    """
    proposito: indica si la nota ingresada es 10

    """
    if ord(nota_ingresada[0]) == 49 and ord(nota_ingresada[1]) == 48 and len(nota_ingresada) == 2:
        salida = True
    else:
        salida = False
    return salida


def nota_valida(nota_a_evaluar:str):
    """
    PROPOSITO: INDICA SI LA NOTA INGRESADA ES VALIDA ENTRE EL 1 Y EL 10
    """
    salida = False

    if len(nota_a_evaluar) == 2 and  solo_numeros(nota_a_evaluar) == True:
        if validar_si_es_10(nota_a_evaluar) == True:
            salida = True
            
    elif len(nota_a_evaluar) == 1 and  solo_numeros(nota_a_evaluar) == True:
        salida = True

    return salida


def ingresar_nota():
    """
    proposito : solicita y valida una nota comprendida entre 1 y 10 inclusive
    validacion: una vez ingresado un dato validado correctamente retorna la nota de no ser asi solicita la una nota nuevamente.
    
    """
    
    while True:

        nota_ingreso = input("\tdigite la nota del estudiante que este entre 1 y 10 \n\t: ")
        
        if  es_entero(nota_ingreso) == True:
            nota = int(nota_ingreso)
            if numero_entre_1_y_10(nota) == True:
                salida = nota_ingreso
                break
            else: print("\t\t-nota fuera del rango de 1 a 10-")

        else: print("\t\t-digito invalido-")
    return salida


def es_entero(cadena:str) -> bool:
    """
    proposito: indica si un dato de tipo cadena reoresenta un numero entero positivo o negativo
    retorna:True en caso de ser un entero de lo contrario False 
    parametro: cadena/ Cadena de tipo str a verificar.
    """
    
    if len(cadena) == 1: #Corroborar que si es el largo de la cadena es 1, que no sea un signo menos
        if ord(cadena) == 32:
            son_enteros = False
            return son_enteros

    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57) or (ord(cadena[i]) == 45) or (ord(cadena[i]) == 32):
            son_enteros = True
        else:
            son_enteros = False
            break

    return son_enteros


def numero_entre_1_y_10(ingreso:int):
    """
    proposito:verifica si el numero entero ingresado esta entre 1 y 10 inclusive.
    retorna: True si esta entre 1 y 10 , false si no.
    parametro: ingreso/numero entero ingresado
    """

    if (ingreso) >= 1 and ingreso <= 10:
        salida = True
    else: salida = False
    return salida


def esta_en_lista(e,l):
    """
    proposito:busca en una lista dada la existencia de un elemendo dado.
    parametros: e/ elemento a buscar
                l/ lista de elementos
    """
    salida = False
    for i in l:
       if i == e:
           salida = True
    return salida