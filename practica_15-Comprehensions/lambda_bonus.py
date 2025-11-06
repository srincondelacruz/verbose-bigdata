#EJERCICIOS BONUS

# 1. Ordenar por Longitud
palabras = ["Python", "es", "un", "lenguaje", "genial"]


ordenadas_por_longitud = sorted(palabras, key= lambda x: len(x))
print(ordenadas_por_longitud)

# 2. Ordenar Tuplas por Precio
productos = [
    ('Café', 8),
    ('Azúcar', 3),
    ('Aceite', 12),
    ('Sal', 2)
]

ordenados_por_precio = sorted(productos, key=lambda x: x[1])
print(ordenados_por_precio)

# 3. Max y Min de Diccionarios
juegos = [
    {'titulo': 'Cyberpunk', 'puntuacion': 7.5},
    {'titulo': 'Elden Ring', 'puntuacion': 9.8},
    {'titulo': 'Starfield', 'puntuacion': 6.9},
    {'titulo': 'Zelda', 'puntuacion': 9.9}
]


juego_max_puntuacion = max(juegos, key=lambda x: x['puntuacion'])
juego_min_puntuacion = min(juegos, key=lambda x: x['puntuacion'])
print(juego_max_puntuacion)
print(juego_min_puntuacion)

# 4. Ordenar Diccionarios (Descendente)
juegos = [
    {'titulo': 'Cyberpunk', 'puntuacion': 7.5},
    {'titulo': 'Elden Ring', 'puntuacion': 9.8},
    {'titulo': 'Starfield', 'puntuacion': 6.9},
    {'titulo': 'Zelda', 'puntuacion': 9.9}
]


ranking_juegos = sorted(juegos, key= lambda x: x['puntuacion'], reverse=True)
print(ranking_juegos)

# 5. Ordenar por Múltiples Criterios
inventario = [
    {'prod': 'Monitor', 'cat': 'Electrónica', 'precio': 150},
    {'prod': 'Ratón', 'cat': 'Periféricos', 'precio': 20},
    {'prod': 'Teclado', 'cat': 'Periféricos', 'precio': 80},
    {'prod': 'SSD', 'cat': 'Electrónica', 'precio': 90}
]

ordenado_complejo = sorted(inventario, key = lambda x: (x['cat'], x['precio']))
print(ordenado_complejo)

# 6. Ordenar por Última Letra
nombres = ["Carlos", "Ana", "Beatriz", "David"]


ordenados_por_ultima = sorted(nombres, key=lambda x: x[-1])
print(ordenados_por_ultima)

# 7. Tupla con Suma Máxima
pares = [(1, 9), (5, 3), (2, 10), (8, 1)] # (El ganador debe ser (2, 10))


tupla_max_suma = max(pares, key=lambda x: (x[0] + x[1]))
print(tupla_max_suma)

# 8. Encontrar el Máximo/Mínimo en Diccionarios
# Dada una lista de diccionarios (juegos), usa max() y min() con una lambda para encontrar:
# a) El juego con la puntuación más alta.
# b) El juego con la puntuación más baja.

juegos = [
    {'titulo': 'Cyberpunk', 'puntuacion': 7.5},
    {'titulo': 'Elden Ring', 'puntuacion': 9.8},
    {'titulo': 'Starfield', 'puntuacion': 6.9},
    {'titulo': 'Zelda', 'puntuacion': 9.9}
]


juego_max_puntuacion = max(juegos, key= lambda x: x['puntuacion'])
juego_min_puntuacion = min(juegos, key= lambda x: x['puntuacion'])
print(juego_max_puntuacion)
print(juego_min_puntuacion)

# 9. Ordenar con Nulos al Final
productos = [
    {'prod': 'Teclado', 'stock': 10},
    {'prod': 'Monitor', 'stock': 5},
    {'prod': 'Ratón Roto', 'stock': None},
    {'prod': 'Alfombrilla', 'stock': 20},
    {'prod': 'Webcam Rota', 'stock': None}
]


ordenado_con_nulos = sorted(productos, key=lambda x: x['stock'] == None)
print(ordenado_con_nulos)

# 10. Ordenar un Diccionario por Valor al reves
puntuaciones = {
    'jugador_1': 1500,
    'jugador_3': 9000,
    'jugador_2': 5000,
    'jugador_4': 2100
}


ranking = sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)
print(ranking)