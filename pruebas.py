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
legajo_inp = input("digite el legajo del alumno (funcion indice fulanito)")

def validar_legajo(legajo_ingreso):
"""
cada digito tiene que ser entre 
"""
    for i in range(6):
        
    