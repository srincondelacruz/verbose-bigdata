# rangos.py - Módulo de clasificación por rangos
# Funciones para clasificar estudiantes por rangos de calificación

def clasificar_por_rango(estudiantes, calificaciones, rango_min, rango_max):
    """
    Clasifica estudiantes dentro de un rango de calificaciones.
    
    Args:
        estudiantes: Lista de nombres de estudiantes
        calificaciones: Lista de calificaciones
        rango_min: Calificación mínima del rango
        rango_max: Calificación máxima del rango
    
    Returns:
        list: Lista de tuplas (estudiante, calificacion) en el rango
    """
    estudiantes_en_rango = []
    
    for i in range(len(estudiantes)):
        if rango_min <= calificaciones[i] <= rango_max:
            estudiantes_en_rango.append((estudiantes[i], calificaciones[i]))
    
    return estudiantes_en_rango


def mostrar_estudiantes_por_rangos(estudiantes, calificaciones):
    """
    Muestra todos los estudiantes clasificados por rangos de calificación.
    
    Args:
        estudiantes: Lista de nombres de estudiantes
        calificaciones: Lista de calificaciones
    """
    print("Estudiantes por rangos de calificación:")
    
    # Rango excelente (90-100)
    print("Excelente (90-100):")
    excelentes = clasificar_por_rango(estudiantes, calificaciones, 90, 100)
    if excelentes:
        for nombre, nota in excelentes:
            print(f"  {nombre}: {nota}")
    else:
        print("  Ninguno")
    
    # Rango bueno (80-89)
    print("Bueno (80-89):")
    buenos = clasificar_por_rango(estudiantes, calificaciones, 80, 89)
    if buenos:
        for nombre, nota in buenos:
            print(f"  {nombre}: {nota}")
    else:
        print("  Ninguno")
    
    # Rango regular (70-79)
    print("Regular (70-79):")
    regulares = clasificar_por_rango(estudiantes, calificaciones, 70, 79)
    if regulares:
        for nombre, nota in regulares:
            print(f"  {nombre}: {nota}")
    else:
        print("  Ninguno")
    
    # Rango deficiente (0-69)
    print("Deficiente (0-69):")
    deficientes = clasificar_por_rango(estudiantes, calificaciones, 0, 69)
    if deficientes:
        for nombre, nota in deficientes:
            print(f"  {nombre}: {nota}")
    else:
        print("  Ninguno")

