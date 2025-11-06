# Práctica 15: Comprehensions

Este documento contiene todos los ejercicios relacionados con *list*, *set* y *dict comprehensions* en Python.

---

## 15.1: Divisibles por 2 y 4

Usa *list comprehension* para generar una lista de números en el rango 2 a 50 que sean divisibles por 2 y por 4.

## 15.2: Aplanar una lista

Aplana la siguiente lista usando *list comprehension*:

```python
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
15.3: Operaciones con Conjuntos (Set)
Crea un conjunto con números aleatorios entre 15 y 45.

Cuenta cuántos son menores que 30.

Elimina todos los números menores que 30.

15.4: Eliminar tuplas vacías
Usa list comprehension para eliminar tuplas vacías de una lista de tuplas.

Python

# Ejemplo de entrada
lista = [(1, 2), (), (3, 4), (), (5,), (6, 7, 8), ()]
15.5: Capitalizar y unir
Dada una cadena, divídela por espacios, capitaliza cada palabra y únelas de nuevo en una cadena. Usa list comprehension.

Python

python = "Es un lenguaje de progrmación muy popular en ML , NN, IA y GenAI"
15.6: Dictionary Comprehension (Complejo)
Dado un diccionario complejo, crea un nuevo diccionario donde:

Las claves sean solo letras y números, en minúsculas, sin espacios ni vocales.

Los valores sean tuplas con: (precio, stock, categoría).

Filtra solo productos con stock > 0 y precio > 100.

Python

# Diccionario de entrada
inventario = {
    "Laptop Dell XPS-15": {"precio": 1200, "stock": 5, "cat": "Electrónica"},
    "Mouse RGB 2024!": {"precio": 45, "stock": 0, "cat": "Periféricos"},
    "Teclado Mecánico Pro": {"precio": 180, "stock": 12, "cat": "Periféricos"},
    "Monitor 4K Ultra": {"precio": 450, "stock": 3, "cat": "Electrónica"},
    "Auriculares BT-500": {"precio": 95, "stock": 8, "cat": "Audio"},
    "Webcam HD Plus+": {"precio": 110, "stock": 0, "cat": "Periféricos"},
    "SSD 1TB NVMe": {"precio": 130, "stock": 20, "cat": "Almacenamiento"}
}
15.7: Suma de matrices 3x4
Suma las dos matrices usando: (a) Bucles for anidados. (b) List comprehension anidada.

Python

mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mat3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
15.8: Dictionary Comprehension (Empleados)
Dado el diccionario de empleados:

Python

emp = {
    'A101': {'name': 'Ashish', 'age': 30, 'salary': 21000},
    'B102': {'name': 'Dinesh', 'age': 25, 'salary': 12200},
    'A103': {'name': 'Ramesh', 'age': 28, 'salary': 11000},
    'D104': {'name': 'Akheel', 'age': 30, 'salary': 18000},
    'A105': {'name': 'Akaash', 'age': 32, 'salary': 20000}
}
Usa dictionary comprehension para crear:

Diccionario con códigos que empiecen con 'A'.

Diccionario con código y nombre.

Diccionario con código y edad.

Diccionario con código y edad > 30.

Diccionario con código y nombre donde el nombre empiece con 'A'.

Diccionario con código y salario en rango [13000, 20000].

15.9: Ejercicios rápidos (Comprehensions)
(a) Genera una lista de coordenadas enteras para todos los puntos en el primer cuadrante desde (1, 1) hasta (5, 5).

(b) Multiplica cada elemento de una lista por 10.

(c) Genera los primeros 20 números de Fibonacci.

(d) Genera dos listas: una con los primeros 20 números impares y otra con los primeros 20 números pares.

(e) Dada una lista con positivos y negativos, crea dos listas: una con positivos y otra con negativos.

(f) Dada una lista de 5 cadenas, conviértelas todas a mayúsculas.

(g) Convierte una lista de temperaturas Fahrenheit a Celsius. (Fórmula: C = (F - 32) * 5/9).

(h) Genera una matriz 2D (4x5) que contenga múltiplos de 4 en el rango de 40 a 160.

(i) ¿Cómo convertirías este bucle en list comprehension?

Python

a = []
for n in range(10, 30):
    if n % 2 == 0:
        a.append(n)
(j) ¿Cómo convertirías este bucle en set comprehension?

Python

a = set()
for n in range(21, 40):
    if n % 2 == 0:
        a.add(n)
print(a)
(k) A partir de la oración:

Python

sent = 'Pack my box with five dozen liquor jugs'
¿Cómo generarías este conjunto (ignora el orden)?

Python

{'liquor', 'jugs', 'with', 'five', 'dozen', 'Pack'}
(l) Usando dict comprehension, ¿cómo convertirías {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} en {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}?

(n) ¿Cómo convertirías d = {'AMOL': 20, 'ANIL': 12, 'SUNIL': 13, 'RAMESH': 10} en {'Amol': 400, 'Anil': 144, 'Sunil': 169, 'Ramesh': 100}?

(o) ¿Cómo convertirías las palabras de una lista (lst = ['Amol', 'Vijay', 'Vinay']) en mayúsculas y las almacenarías en un conjunto?

# Parte 2 - Programación Funcional - Lambda

---

## 7️⃣ Ejercicio 15.10: Max y Min de un Diccionario

Supón que un diccionario contiene pares clave-valor, donde la clave es una letra del alfabeto y el valor es un número.

Escribe un programa que obtenga los valores máximo y mínimo del diccionario usando las funciones `max()` y `min()` en combinación con `lambda`.

```python
# Ejemplo de diccionario
datos = {'a': 10, 'b': 3, 'c': 25, 'd': 1}
8️⃣ Ejercicio 15.11: Tareas con Map, Filter y Reduce
Usando lambda, map(), filter() y reduce() (o una combinación) para realizar las siguientes tareas:

(Nota: Para reduce, primero debes importarlo: from functools import reduce)

(a) Suma de edades (Perros)
Supón que un diccionario contiene el tipo de mascota, nombre y edad. Escribe un programa que obtenga la suma de todas las edades de los perros.

Python

# Ejemplo de entrada
mascotas = [
    {'tipo': 'perro', 'nombre': 'Max', 'edad': 5},
    {'tipo': 'gato', 'nombre': 'Misu', 'edad': 3},
    {'tipo': 'perro', 'nombre': 'Rocky', 'edad': 2}
]
(b) Áreas de Círculos
Considera la siguiente lista de radios: lst = [1.25, 3.22, 4.68, 10.95, 32.55, 12.54]

Escribe un programa para obtener una lista de las áreas de estos círculos (Area = pi * r^2) redondeadas a dos decimales. (Usa math.pi).

(c) Combinar dos listas (Zip)
Considera las siguientes listas: nums = [10, 20, 30, 40, 50, 60, 70, 80] strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

Escribe un programa para obtener una lista de tuplas, donde cada tupla contenga un número y una cadena (ej. [(10, 'A'), (20, 'B'), ...]

(Pista: ¡zip() es tu amigo aquí!)

(d) Filtrar Calificaciones
Supón un diccionario con nombres de estudiantes y sus calificaciones. Escribe un programa para obtener una lista de los estudiantes que obtuvieron más de 40 puntos.

Python

# Ejemplo de entrada
calificaciones = {'Ana': 50, 'Luis': 35, 'Sara': 41, 'Juan': 20}
(e) Encontrar Palíndromos
Considera la siguiente lista: lst = ['Malayalam', 'Drawing', 'madamlamadam', '1234321']

Escribe un programa para imprimir aquellas cadenas que son palíndromos.

(Pista: cadena.lower() == cadena.lower()[::-1])

(f) Filtrar Nombres Largos
Una lista contiene nombres de empleados. Escribe un programa para filtrar aquellos nombres cuya longitud sea mayor a 8 caracteres.

(g) Filtrar Empleados "Expertos"
Un diccionario contiene la siguiente información sobre 5 empleados: Escribe un programa para obtener una lista de empleados (nombre + apellido) que sean "Altamente expertos".

Python

# Ejemplo de entrada
empleados = [
    {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 30, 'grado': 'Experto'},
    {'nombre': 'Maria', 'apellido': 'Gomez', 'edad': 45, 'grado': 'Altamente experto'},
    {'nombre': 'Carlos', 'apellido': 'Ruiz', 'edad': 28, 'grado': 'Semiexperto'}
]
(h) Unir una lista de palabras
Considera la siguiente lista: lst = ['Benevolent', 'Dictator', 'For', 'Life']

Escribe un programa para obtener una sola cadena: 'Benevolent Dictator For Life'.

(Pista: reduce() es perfecto para esto, aunque join es más simple).

(i) Nombres a Mayúsculas
Considera la siguiente lista de estudiantes: lst = ['Rahul', 'Priya', 'Chaaya', 'Narendra', 'Prashant']

Escribe un programa para obtener una lista en la que todos los nombres se conviertan a mayúsculas.
