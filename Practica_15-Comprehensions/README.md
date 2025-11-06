# Práctica 15: Comprehensions y Funciones Lambda

Este directorio contiene los ejercicios de la Práctica 15, divididos en dos partes principales:

1.  **Programación Funcional (Parte 1):** Ejercicios para dominar *list*, *set* y *dict comprehensions*.
2.  **Funciones Lambda (Parte 2):** Ejercicios de examen centrados en el uso de `lambda` con funciones de ordenamiento (`sorted`, `max`, `min`).

## 🗂️ Índice de Archivos

* **[TUTORIAL.md](./TUTORIAL.md)**: El guion completo de la práctica con todas las explicaciones teóricas.
* **[EJERCICIOS.md](./EJERCICIOS.md)**: El guion de los ejercicios (sin la teoría).
* **[practica_15.py](./practica_15.py)**: Soluciones a la Parte 1 (Comprehensions).
* **[lambda_bonus.py](./lambda_bonus.py)**: Soluciones a la Parte 2 (Lambda).

---

## 🧠 Enfoque y Lógica de Solución

La estrategia para resolver los ejercicios se dividió en dos fases:

### 1. `practica_15.py` (La Fábrica: Comprehensions)

En esta parte, la lógica fue usar la sintaxis `[expresion for item in iterable if filtro]` para construir nuevos iterables en una sola línea.

* **Listas (`[]`)**: Se usaron para transformar (`[x * 10 ... ]`) y filtrar (`[... if x % 2 == 0]`).
* **Bucles Anidados (`for ... for ...`)**: Se usaron para aplanar matrices (`[n for sublista in mat for n in sublista]`) o crear cuadrículas (`[(x, y) for x... for y...]`).
* **Conjuntos (`{}`) vs. Diccionarios (`{k: v}`)**:
    * Para crear **conjuntos**, se usó la sintaxis simple: `{expresion for ...}`.
    * Para crear **diccionarios**, fue crucial usar los dos puntos (`:`) para separar la clave del valor: `{clave_nueva: valor_nuevo for ...}`.
* **Filtros (`if`)**: Los filtros (`if v['stock'] > 0`) se colocaron al final de la *comprehension* para descartar elementos.

### 2. `lambda_bonus.py` (La Chuleta: Lambda)

El objetivo aquí no era *crear* listas, sino *informar* a otras funciones (como `sorted()`, `max()`, `min()`) sobre **cómo** debían comparar los elementos.

La `lambda` siempre se usó como el argumento `key=`.

* **Lógica 1: Clave Simple (Atributo)**
    * Para ordenar por una propiedad simple, la `lambda` devuelve esa propiedad.
    * `key=lambda x: len(x)` (Ordena por longitud).
    * `key=lambda x: x[-1]` (Ordena por el último carácter).

* **Lógica 2: Clave por Posición (Tuplas)**
    * Cuando se itera sobre tuplas (como en `.items()`), `x` es la tupla.
    * `key=lambda x: x[1]` (Ordena por el segundo elemento, el precio/valor).
    * `key=lambda x: x[0] + x[1]` (Ordena por la suma de los elementos).

* **Lógica 3: Clave por Nombre (Diccionarios)**
    * Cuando se itera sobre una lista de diccionarios, `x` es el diccionario.
    * `key=lambda x: x['puntuacion']` (Ordena usando el valor de la clave 'puntuacion').

* **Lógica 4: Clave Múltiple (Desempate)**
    * Para ordenar por múltiples criterios (categoría y luego precio), la `lambda` devuelve una **tupla** con el orden de prioridad.
    * `key=lambda x: (x['cat'], x['precio'])`

* **Lógica 5: Clave Booleana (Nulos al final)**
    * Para agrupar valores `None` al final, la `lambda` devuelve un Booleano.
    * `key=lambda x: x['stock'] == None`
    * `sorted()` agrupa todos los `False` (0) primero y los `True` (1) después.