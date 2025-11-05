def ordenar_por_nota(alumnos):
    """Ordena una lista de diccionarios de alumnos por su clave 'nota' descendente."""
    # Usamos sorted y una función lambda para ordenar por la clave 'nota'
    return sorted(alumnos, key=lambda alumno: alumno.get('nota', 0), reverse=True)