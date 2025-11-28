import random

def validar_calificacion(calificacion):
    """Valida que la calificación esté entre 1 y 10"""
    return 1 <= calificacion <= 10

def validar_genero(genero):
    """Valida que el género sea F, M o X"""
    return genero in ['F', 'M', 'X']

def validar_legajo(legajo):
    """Valida que el legajo sea numérico de 6 cifras"""
    return isinstance(legajo, int) and 100000 <= legajo <= 999999

def validar_estado(estado):
    """Valida que el estado sea 0 o 1"""
    return estado in [0, 1]



def cargar_datos_hardcodeados(calificaciones, nombres, generos, legajos, estados):
    """Carga datos de ejemplo para testing"""
    # Limpiar listas existentes
    calificaciones.clear()
    nombres.clear()
    generos.clear()
    legajos.clear()
    estados.clear()
    
    # Datos de ejemplo
    apellidos_nombres = [
        "Gonzalez Maria", "Lopez Carlos", "Martinez Ana", "Rodriguez Pedro", 
        "Fernandez Laura", "Perez Juan", "Gomez Sofia", "Hernandez Luis",
        "Diaz Carmen", "Torres Miguel", "Ramirez Elena", "Flores Diego",
        "Silva Patricia", "Rojas Andres", "Mendoza Veronica", "Castillo Roberto",
        "Ortiz Daniela", "Navarro Javier", "Romero Natalia", "Alvarez Fernando",
        "Vargas Monica", "Castro Ricardo", "Morales Gabriela", "Salazar Oscar",
        "Reyes Claudia", "Medina Hugo", "Suarez Adriana", "Iglesias Sebastian",
        "Paredes Lorena", "Acosta Martin"
    ]
    
    generos_posibles = ['F', 'M', 'X']
    
    for i in range(30):
        # Calificaciones aleatorias entre 1 y 10
        calif_estudiante = [random.randint(1, 10) for _ in range(5)]
        calificaciones.append(calif_estudiante)
        
        # Datos personales
        nombres.append(apellidos_nombres[i])
        generos.append(random.choice(generos_posibles))
        legajos.append(100000 + i)
        estados.append(random.choice([0, 1]))
    
    print("Datos cargados exitosamente!")
    return True

def mostrar_estudiante(indice, calificaciones, nombres, generos, legajos, estados, promedios=None):
    """Muestra los datos de un estudiante específico"""
    print(f"\n--- Estudiante {indice + 1} ---")
    print(f"Legajo: {legajos[indice]}")
    print(f"Nombre: {nombres[indice]}")
    print(f"Género: {generos[indice]}")
    print(f"Estado: {'Ocupado' if estados[indice] == 1 else 'Libre'}")
    print(f"Calificaciones: {calificaciones[indice]}")
    if promedios and indice < len(promedios):
        print(f"Promedio: {promedios[indice]:.2f}")

def mostrar_todos_activos(calificaciones, nombres, generos, legajos, estados, promedios=None):
    """Muestra todos los estudiantes con estado activo (1)"""
    print("\n" + "="*80)
    print("LISTA DE ESTUDIANTES ACTIVOS")
    print("="*80)
    
    encontrados = False
    for i in range(len(calificaciones)):
        if estados[i] == 1:  # Solo mostrar activos
            encontrados = True
            mostrar_estudiante(i, calificaciones, nombres, generos, legajos, estados, promedios)
    
    if not encontrados:
        print("No hay estudiantes activos para mostrar.")

def calcular_promedios(calificaciones):
    """Calcula el promedio de cada estudiante"""
    promedios = []
    for calif_estudiante in calificaciones:
        promedio = sum(calif_estudiante) / len(calif_estudiante)
        promedios.append(promedio)
    return promedios


def ordenar_por_promedio(calificaciones, nombres, generos, legajos, estados, promedios, ascendente=False):
    """Ordena todos los datos por promedio (ASC o DESC)"""
    # Crear una lista de tuplas con todos los datos
    datos_combinados = list(zip(promedios, calificaciones, nombres, generos, legajos, estados))
    
    # Ordenar por promedio
    datos_combinados.sort(reverse=not ascendente)
    
    # Separar los datos ordenados
    promedios_ordenados = [dato[0] for dato in datos_combinados]
    calificaciones_ordenadas = [dato[1] for dato in datos_combinados]
    nombres_ordenados = [dato[2] for dato in datos_combinados]
    generos_ordenados = [dato[3] for dato in datos_combinados]
    legajos_ordenados = [dato[4] for dato in datos_combinados]
    estados_ordenados = [dato[5] for dato in datos_combinados]
    
    return (calificaciones_ordenadas, nombres_ordenados, generos_ordenados, 
            legajos_ordenados, estados_ordenados, promedios_ordenados)

def mostrar_materia(indice, promedio):
    """Muestra los datos de una materia específica"""
    print(f"MATERIA_{indice + 1}: Promedio = {promedio:.2f}")



def mostrar_materias_con_promedio(calificaciones):
    """Muestra todas las materias con sus promedios generales"""
    if not calificaciones:
        print("No hay datos cargados.")
        return
    
    num_materias = len(calificaciones[0])
    promedios_materias = []
    
    # Calcular promedio por materia
    for i in range(num_materias):
        suma = 0
        for estudiante in calificaciones:
            suma += estudiante[i]
        promedio = suma / len(calificaciones)
        promedios_materias.append(promedio)
        mostrar_materia(i, promedio)
    
    return promedios_materias


# muestra las materias con mayor promedio


def materias_mayor_promedio(calificaciones):
    """Encuentra la/s materia/s con mayor promedio general"""
    
    if not calificaciones:
        print("No hay datos cargados.")
        return
    
    promedios_materias = mostrar_materias_con_promedio(calificaciones)
    max_promedio = max(promedios_materias)
    
    print(f"\nMateria/s con mayor promedio general ({max_promedio:.2f}):")
    for i, promedio in enumerate(promedios_materias):
        if promedio == max_promedio:
            print(f"MATERIA_{i + 1}")



# busca un estudiante por legajo

def buscar_por_legajo(legajos, calificaciones, nombres, generos, estados, promedios, legajo_buscar):
    """Busca un estudiante por legajo"""
    for i in range(len(legajos)):
        if legajos[i] == legajo_buscar:
            return i
    return -1






def mostrar_todos_datos_legajo(indice, calificaciones, nombres, generos, legajos, estados, promedios):
    """Muestra todos los datos de un estudiante incluyendo promedio"""
    if indice != -1:
        print(f"\n--- DATOS COMPLETOS DEL ESTUDIANTE ---")
        mostrar_estudiante(indice, calificaciones, nombres, generos, legajos, estados, promedios)
    else:
        print("No se encontró ningún estudiante con ese legajo.")




#  valida si lla materia existe y si no hay notas dice que no hay dnotas cargadas 

def frecuencia_calificaciones(calificaciones, numero_materia):
    """Calcula la frecuencia de cada calificación en una materia específica"""
    if numero_materia < 1 or numero_materia > 5:
        print("Número de materia inválido. Debe ser entre 1 y 5.")
        return None
    
    if not calificaciones:
        print("No hay datos cargados.")
        return None
    
    # Inicializar lista de frecuencias (índices 0-9 para notas 1-10)
    frecuencias = [0] * 10
    
    # Contar frecuencias
    indice_materia = numero_materia - 1
    for estudiante in calificaciones:
        nota = estudiante[indice_materia]
        if 1 <= nota <= 10:
            frecuencias[nota - 1] += 1
    
    return frecuencias

def mostrar_frecuencias_calificaciones(frecuencias, numero_materia):
    """Muestra las frecuencias de calificaciones de una materia"""
    if frecuencias:
        print(f"\nFrecuencia de calificaciones - MATERIA_{numero_materia}")
        print("-" * 50)
        for i in range(10):
            print(f"Nota {i + 1}: {frecuencias[i]} veces")

def main():
    # Estructuras de datos principales
    calificaciones = []  # Matriz 30x5
    nombres = []         # Lista de nombres
    generos = []         # Lista de géneros
    legajos = []         # Lista de legajos
    estados = []         # Lista de estados
    promedios = []       # Lista de promedios (se calcula)
    
    datos_cargados = False
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GESTIÓN DE ESTUDIANTES")
        print("="*50)
        print("1 - Cargar datos")
        print("2 - Mostrar estudiantes activos")
        print("3 - Calcular promedios")
        print("4 - Ordenar por promedio (DESC)")
        print("5 - Mostrar materias con mayor promedio")
        print("6 - Buscar estudiante por legajo")
        print("7 - Frecuencia de calificaciones por materia")
        print("8 - Salir")
        print("-"*50)
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == '1':
            cargar_datos_hardcodeados(calificaciones, nombres, generos, legajos, estados)
            datos_cargados = True
            promedios = []  # Resetear promedios
            
        elif opcion == '2':
            if datos_cargados:
                mostrar_todos_activos(calificaciones, nombres, generos, legajos, estados, promedios)
            else:
                print("Primero debe cargar los datos (opción 1)")
                
        elif opcion == '3':
            if datos_cargados:
                promedios = calcular_promedios(calificaciones)
                print("Promedios calculados exitosamente!")
                print("Lista de promedios:")
                for i, prom in enumerate(promedios):
                    print(f"Estudiante {i+1}: {prom:.2f}")
            else:
                print("Primero debe cargar los datos (opción 1)")
                
        elif opcion == '4':
            if datos_cargados:
                if not promedios:
                    promedios = calcular_promedios(calificaciones)
                
                (calificaciones_ord, nombres_ord, generos_ord, 
                 legajos_ord, estados_ord, promedios_ord) = ordenar_por_promedio(
                    calificaciones, nombres, generos, legajos, estados, promedios, ascendente=False)
                
                print("\nESTUDIANTES ORDENADOS POR PROMEDIO (DESCENDENTE)")
                print("="*60)
                for i in range(len(promedios_ord)):
                    print(f"{i+1:2d}. {nombres_ord[i]:20} - Promedio: {promedios_ord[i]:.2f}")
            else:
                print("Primero debe cargar los datos (opción 1)")
                
        elif opcion == '5':
            if datos_cargados:
                materias_mayor_promedio(calificaciones)
            else:
                print("Primero debe cargar los datos (opción 1)")
                
        elif opcion == '6':
            if datos_cargados:
                try:
                    legajo_buscar = int(input("Ingrese el legajo a buscar (6 dígitos): "))
                    if not validar_legajo(legajo_buscar):
                        print("Legajo inválido. Debe ser un número de 6 dígitos.")
                    else:
                        indice = buscar_por_legajo(legajos, calificaciones, nombres, generos, estados, promedios, legajo_buscar)
                        if not promedios:
                            promedios_temp = calcular_promedios(calificaciones)
                        else:
                            promedios_temp = promedios
                        mostrar_todos_datos_legajo(indice, calificaciones, nombres, generos, legajos, estados, promedios_temp)
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
            else:
                print("Primero debe cargar los datos (opción 1)")
                
        elif opcion == '7':
            if datos_cargados:

                # valida el dato con el try
                
                try:
                    num_materia = int(input("Ingrese el número de materia (1-5): "))
                    frecuencias = frecuencia_calificaciones(calificaciones, num_materia)
                    if frecuencias:
                        mostrar_frecuencias_calificaciones(frecuencias, num_materia)
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
            
            else:
                print("Primero debe cargar los datos (opción 1)")
                
        elif opcion == '8':
            print("¡Gracias por usar el sistema!")
            break
            
        else:
            print("Opción inválida. Por favor, seleccione 1-8.")


main()