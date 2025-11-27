#funciona
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

#funciona
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



#funciona
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






