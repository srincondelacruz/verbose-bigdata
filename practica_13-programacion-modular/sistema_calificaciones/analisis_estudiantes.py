# analisis_estudiantes.py - Módulo de análisis de estudiantes
# Funciones para analizar el rendimiento de los estudiantes

def contar_aprobados_reprobados(estudiantes, calificaciones, nota_aprobacion=80):
    """
    Cuenta los estudiantes aprobados y reprobados.
    
    Args:
        estudiantes: Lista de nombres de estudiantes
        calificaciones: Lista de calificaciones
        nota_aprobacion: Nota mínima para aprobar (default: 80)
    
    Returns:
        tuple: (aprobados, reprobados)
    """
    aprobados = 0
    reprobados = 0
    
    print("Contando aprobados y reprobados...")
    for i in range(len(calificaciones)):
        if calificaciones[i] >= nota_aprobacion:
            aprobados += 1
            print(f"  {estudiantes[i]} APROBÓ con {calificaciones[i]}")
        else:
            reprobados += 1
            print(f"  {estudiantes[i]} REPROBÓ con {calificaciones[i]}")
    
    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes reprobados: {reprobados}")
    
    return aprobados, reprobados


def encontrar_mejor_estudiante(estudiantes, calificaciones):
    """
    Encuentra al estudiante con la mejor calificación.
    
    Returns:
        tuple: (nombre_estudiante, calificacion)
    """
    mejor_nota = calificaciones[0]
    mejor_estudiante = estudiantes[0]
    
    for i in range(1, len(calificaciones)):
        if calificaciones[i] > mejor_nota:
            mejor_nota = calificaciones[i]
            mejor_estudiante = estudiantes[i]
    
    return mejor_estudiante, mejor_nota


def encontrar_peor_estudiante(estudiantes, calificaciones):
    """
    Encuentra al estudiante con la peor calificación.
    
    Returns:
        tuple: (nombre_estudiante, calificacion)
    """
    peor_nota = calificaciones[0]
    peor_estudiante = estudiantes[0]
    
    for i in range(1, len(calificaciones)):
        if calificaciones[i] < peor_nota:
            peor_nota = calificaciones[i]
            peor_estudiante = estudiantes[i]
    
    return peor_estudiante, peor_nota


def calcular_porcentaje_aprobacion(aprobados, total):
    """Calcula el porcentaje de aprobación."""
    return (aprobados / total) * 100


def generar_resumen(aprobados, reprobados, porcentaje):
    """
    Genera un resumen del rendimiento general.
    
    Returns:
        str: Mensaje de resumen
    """
    if aprobados > reprobados:
        return f"Buen rendimiento general: {porcentaje:.1f}% de aprobación"
    elif reprobados > aprobados:
        return f"Rendimiento preocupante: solo {porcentaje:.1f}% de aprobación"
    else:
        return f"Rendimiento equilibrado: {porcentaje:.1f}% de aprobación"


def mostrar_analisis_estudiantes(estudiantes, calificaciones):
    """
    Realiza y muestra el análisis completo de los estudiantes.
    
    Returns:
        dict: Diccionario con los resultados del análisis
    """
    aprobados, reprobados = contar_aprobados_reprobados(estudiantes, calificaciones)
    
    print("\nBuscando mejor y peor estudiante...")
    mejor_estudiante, mejor_nota = encontrar_mejor_estudiante(estudiantes, calificaciones)
    peor_estudiante, peor_nota = encontrar_peor_estudiante(estudiantes, calificaciones)
    
    # Mostrar el proceso de búsqueda
    for i in range(len(calificaciones)):
        if calificaciones[i] == mejor_nota and estudiantes[i] == mejor_estudiante:
            print(f"  Nuevo mejor: {mejor_estudiante} ({mejor_nota})")
        if calificaciones[i] == peor_nota and estudiantes[i] == peor_estudiante:
            print(f"  Nuevo peor: {peor_estudiante} ({peor_nota})")
    
    print(f"Mejor rendimiento: {mejor_estudiante} ({mejor_nota})")
    print(f"Menor rendimiento: {peor_estudiante} ({peor_nota})")
    
    total_estudiantes = len(estudiantes)
    porcentaje_aprobados = calcular_porcentaje_aprobacion(aprobados, total_estudiantes)
    resumen = generar_resumen(aprobados, reprobados, porcentaje_aprobados)
    
    print(f"\nResumen: {resumen}")
    
    return {
        "aprobados": aprobados,
        "reprobados": reprobados,
        "mejor_estudiante": mejor_estudiante,
        "mejor_nota": mejor_nota,
        "peor_estudiante": peor_estudiante,
        "peor_nota": peor_nota,
        "porcentaje_aprobados": porcentaje_aprobados,
        "total_estudiantes": total_estudiantes
    }

