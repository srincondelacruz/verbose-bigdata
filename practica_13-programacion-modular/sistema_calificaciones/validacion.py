# validacion.py - Módulo de validación
# Funciones para validar datos de entrada

def validar_datos(estudiantes, calificaciones):
    """
    Valida que los datos de estudiantes y calificaciones sean correctos.
    
    Args:
        estudiantes: Lista de nombres de estudiantes
        calificaciones: Lista de calificaciones
    
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if len(estudiantes) == 0:
        return False, "La lista de estudiantes está vacía"
    
    if len(calificaciones) == 0:
        return False, "La lista de calificaciones está vacía"
    
    if len(estudiantes) != len(calificaciones):
        return False, "Las listas deben tener la misma longitud"
    
    # Validar cada calificación
    for calificacion in calificaciones:
        if calificacion < 0 or calificacion > 100:
            return False, f"La calificación {calificacion} está fuera del rango válido (0-100)"
    
    return True, "Datos válidos"


def mostrar_validacion(es_valido, mensaje):
    """
    Muestra el resultado de la validación.
    
    Args:
        es_valido: Booleano indicando si los datos son válidos
        mensaje: Mensaje descriptivo del resultado
    """
    print("Validando datos de entrada...")
    if es_valido:
        print(f"Resultado: {mensaje}")
    else:
        print(f"ERROR: {mensaje}")
        print("No se pueden procesar datos inválidos")
        exit()

