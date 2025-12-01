


def valor_de_1_a_5(valor_ingresado:str) -> bool:
    """
    proposito: valida si el valor ingresado esta entre 1 y 5 en formato str
    Args:
        valor_ingresado : valor a validar

    Returns:
        bool: True si es valido False si no
    """
    salida = False
    if ord(valor_ingresado) >= 49 and ord(valor_ingresado) <= 53:
        salida = True

    return salida





def buscar_indice_disponible(lista_estados:list) -> int:
    """  
    proposito: busca el primer indice disponible en la lista de estados
    Args:
        lista_estados : lista de estados

    Returns:
        int: indice disponible o False si no hay disponibles
    """
    contador = 0
    resultado = None
    for i in range(len(lista_estados)):        
        if lista_estados[i] == 0 and contador == 0:
            contador +=1
            resultado = i
    if contador == 0:
        resultado = False
    return resultado




def pasar_a_minuscula(texto_ingresado :str) -> str:
    """
    proposito: convierte una cadena de texto a minusculas
    Args:
        texto_ingresado : cadena de texto a convertir a minusculas

    Returns:
        str: cadena de texto en minusculas
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


def solo_cadena(dato_a_evaluar:str) -> bool:

    """
    proposito: determina si todos los caracteres representan una letra
    Returns:
        bool: True si todos los caracteres son letras, False si no
    """

    salida = True
    ingreso = pasar_a_minuscula(dato_a_evaluar)
    for digito in ingreso:
        if ord(digito) > 122 or ord(digito) < 97:
            salida = False

    
    return salida


def solo_numeros(dato_a_evaluar:str) -> bool:

    """
    proposito: determina si todos los caracteres representan un numero
    Returns:
        bool: True si todos los caracteres son numeros, False si no
    """
    salida = True
    for digito in dato_a_evaluar:
        if ord(digito) > 57 or ord(digito) < 48:
            salida = False

    return salida


def validar_si_es_10(nota_ingresada:str) -> bool:
    """
    proposito: valida si la nota ingresada es 10
    Args:   
        nota_ingresada (str): nota a validar en formato str

    Returns:
        bool: True si la nota es 10, False si no
    """
    if ord(nota_ingresada[0]) == 49 and ord(nota_ingresada[1]) == 48 and len(nota_ingresada) == 2:
        salida = True
    else:
        salida = False
    return salida


def nota_valida(nota_a_evaluar:str) -> bool:
    """
    proposito: valida si la nota ingresada es valida (entre 1 y 10)
    Args:
        nota_a_evaluar : nota a validar en formato str

    Returns:
        bool: True si la nota es valida, False si no
    """
    salida = False

    if len(nota_a_evaluar) == 2 and  solo_numeros(nota_a_evaluar) == True:
        if validar_si_es_10(nota_a_evaluar) == True:
            salida = True
            
    elif len(nota_a_evaluar) == 1 and  solo_numeros(nota_a_evaluar) == True:
        salida = True

    return salida


def ingresar_nota() -> str:
    
    """
    proposito: ingresa una nota validada para un alumno en una materia dada
    Returns:
        str: nota validada
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
    proposito: determina si la cadena ingresada representa un numero entero
    Args:
        cadena : cadena a evaluar

    Returns:
        bool: True si la cadena representa un numero entero, False si no
    """
    
    if len(cadena) == 1:
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


def numero_entre_1_y_10(ingreso:int) -> bool:
    """
    proposito: valida si el numero ingresado esta entre 1 y 10
    Args:
        ingreso : numero a validar en formato int

    Returns:
        bool: True si el numero es valido False si no
    """

    if (ingreso) >= 1 and ingreso <= 10:
        salida = True
    else: salida = False
    return salida


def esta_en_lista(e:None,l:list) -> bool:
    """
    proposito: verifica si un elemento esta en una lista
    Args:
        e : elemento a buscar
        l : lista donde buscar

    Returns:
        bool: True si el elemento esta en la lista, False si no
    """
    salida = False
    for i in l:
       if i == e:
           salida = True
    return salida


