# 15.1: Números divisibles por 2 y por 4 entre 2 y 50.

x = [ x for x in range(2, 50) if x % 2 == 0 and x % 4 == 0 ]
print(x)

# 15.2: Aplana la siguiente lista usando list comprehension:
# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

aplanada = [*mat[0], *mat[1], *mat[2]]
aplanada_v2 = [n for num in mat for n in num]
print(aplanada)
print(aplanada_v2)
print(" ".join(map(str, aplanada_v2)))

# 15.3: Crea un conjunto (set) con números aleatorios entre 15 y 45.
#
# Cuenta cuántos son menores que 30.
# Elimina todos los números menores que 30.
#
# Pista: Para los aleatorios, primero tendrás que importar la librería 'random'.
# 'random.randint(a, b)' te dará un número entre a y b.

import random

a = {random.randint(15, 45) for i in range(10)}
x = {n for n in a if n >= 30}
print(f"Nums aleatorios {a}")
print(f"Mayores de 30 {x}")

# 15.4: Usa list comprehension para eliminar tuplas vacías de una lista de tuplas.
lista = [(1, 2), (), (3, 4), (), (5,), (6, 7, 8), ()]

# Pista: En Python, una tupla vacía () evalúa como 'False' en 
# un contexto booleano,
# y una tupla con contenido (como (1, 2) o (5,)) evalúa como 'True'.

lista_limpia = [n for n in lista if n]
print(f"Lista {lista}")
print(f"Lista limpia {lista_limpia}")

# 15.5: Dada una cadena, divídela por espacios, capitaliza cada palabra
# y únelas de nuevo en una cadena. Usa list comprehension.

python = "Es un lenguaje de progrmación muy popular en ML , NN, IA y GenAI"

resultado = " ".join([n.capitalize() for n in python.split()])
print(resultado)

# 15.6: Dictionary Comprehension (Complejo)
#
# Dado un diccionario complejo, crea un nuevo diccionario donde:
#   - Las claves sean solo letras y números, en minúsculas, sin espacios ni vocales (aeiou).
#   - Los valores sean tuplas con: (precio, stock, categoría).
#   - Filtra solo productos con stock > 0 Y precio > 100.

inventario = {
    "Laptop Dell XPS-15": {"precio": 1200, "stock": 5, "cat": "Electrónica"},
    "Mouse RGB 2024!": {"precio": 45, "stock": 0, "cat": "Periféricos"},
    "Teclado Mecánico Pro": {"precio": 180, "stock": 12, "cat": "Periféricos"},
    "Monitor 4K Ultra": {"precio": 450, "stock": 3, "cat": "Electrónica"},
    "Auriculares BT-500": {"precio": 95, "stock": 8, "cat": "Audio"},
    "Webcam HD Plus+": {"precio": 110, "stock": 0, "cat": "Periféricos"},
    "SSD 1TB NVMe": {"precio": 130, "stock": 20, "cat": "Almacenamiento"}
}


resultado_final = {"".join(char for char in clave.lower() if char.isalnum() and char not in {'a', 'e', 'i', 'o', 'u'}): 
                   (datos["precio"], datos["stock"], datos["cat"]) 
                   for clave, datos in inventario.items() 
                   if datos["stock"] > 0 and datos["precio"] > 100}
print(resultado_final)


# 15.7: Suma dos matrices 3x4 usando:
# (a) Listas anidadas (bucles 'for' tradicionales)
# (b) List comprehension

mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mat3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # Matriz para rellenar en (a)

num_filas = len(mat1)
num_columnas = len(mat1[0])

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j] + mat2[i][j]
print(mat3)


mat3_comprehension = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]for i in range(len(mat1))]
print(mat3_comprehension)


# 15.8: Dado el diccionario de empleados:
emp = {
    'A101': {'name': 'Ashish', 'age': 30, 'salary': 21000},
    'B102': {'name': 'Dinesh', 'age': 25, 'salary': 12200},
    'A103': {'name': 'Ramesh', 'age': 28, 'salary': 11000},
    'D104': {'name': 'Akheel', 'age': 30, 'salary': 18000},
    'A105': {'name': 'Akaash', 'age': 32, 'salary': 20000}
}

# Usa dictionary comprehension para crear:
# 1. Diccionario con códigos que empiecen con 'A'
# 2. Diccionario con código y nombre
# 3. Diccionario con código y edad
# 4. Diccionario con código y edad > 30
# 5. Diccionario con código y nombre donde el nombre empiece con 'A'
# 6. Diccionario con código y salario en rango [13000, 20000]

# Pista: La sintaxis base será:
# { clave_nueva: valor_nuevo for clave_original, valor_original in emp.items() if (condicion) }


n = {k: v for k, v in emp.items() if k.startswith('A')}
emp_nomb = {k: v['name'] for k, v in emp.items()}
emp_edad = {k: v['age'] for k, v in emp.items()}
emp_edad_30 = { k: v["age"] for k, v in emp.items() if v['age'] > 30 }
emp_start_a = {k: v['name'] for k, v in emp.items() if k.startswith('A') and v['name'].startswith('A')}
emp_salario = {k: v['salary'] for k, v in emp.items() if v["salary"] >= 13000 and v["salary"] <= 20000}

print(n)
print(emp_nomb)
print(emp_edad)
print(emp_edad_30)
print(emp_start_a)
print(emp_salario)


# 15.9: Ejercicios rápidos (Comprehensions)

# (a) Escribe un programa que genere una lista de coordenadas enteras
#     para todos los puntos en el primer cuadrante desde (1, 1) hasta (5, 5).
# Pista: (x, y) ... necesitarás un 'for x in range(1, 6)' y un 'for y in range(1, 6)'
coordenadas= [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(coordenadas)


# (b) Usando list comprehension, escribe un programa para crear una lista
#     multiplicando cada elemento de la lista por 10.
lista_diez = [x*10  for x in range(1, 11)]
print(lista_diez)

# (c) Escribe un programa para generar los primeros 20 números de Fibonacci.
# Pista: ¡Trampa! Esto es muy difícil de hacer con list comprehension.
fib = [0, 1]
for i in range(18):
    fib.append( fib[-1] + fib[-2] )
print(fib)

# (d) Escribe un programa para generar dos listas usando list comprehension.
#     Una debe contener los primeros 20 números impares y la otra los primeros 20 números pares.
# Pista: range(1, 41)
lista_1 = [n for n in range(1, 40) if n % 2 != 0]
lista_2 = [n for n in range(1, 41) if n % 2 == 0]
print(lista_1)
print(lista_2)

# (e) Supón una lista que contiene números positivos y negativos.
#     Escribe un programa para crear dos listas:
#     una conteniendo números positivos y otra conteniendo números negativos.

lista_mezclada = [1, -5, 3, -10, 9, -2, 0] # (Usaremos 0 como positivo)

positivos = [n for n in lista_mezclada if n >= 0]
negativos = [n for n in lista_mezclada if n < 0]
print(positivos)
print(negativos)

# (f) Supón una lista que contiene 5 cadenas. Escribe un programa
#     para convertir todas estas cadenas a mayúsculas.
lst = ['Amol', 'Vijay', 'Vinay', 'Rahul', 'Sandeep']

lst_mayus = [n.upper() for n in lst]
print(lst_mayus)

# (g) Escribe un programa que convierta una lista de temperaturas en
#     grados Fahrenheit a sus equivalentes en grados Celsius
#     usando list comprehension.
#     Fórmula: C = (F - 32) * 5/9

fahrenheit = [32, 68, 86, 104, 212]

celsius = [(n - 32) * 5/9 for n in fahrenheit]
print(celsius)

# (h) Escribe un programa para generar una matriz 2D de tamaño 4x5
#     que contenga múltiplos de 4 en el rango de 40 a 160.

matriz_multiplos = [[(40 + (i*5 + j) * 4) for j in range(5)] for i in range(4)]
print(matriz_multiplos)

# (i) ¿Cómo convertirías el siguiente código en una list comprehension?
#
# a = []
# for n in range(10, 30):
#     if n % 2 == 0:
#         a.append(n)
#
a_comp = [n for n in range(10, 30) if n % 2 == 0]
print(a_comp)

#( j ) ¿Cómo convertirías el siguiente código en una set comprehension?
# a = set()
# for n in range(21, 40):
#     if n % 2 == 0:
#         a.add(n)
# print(a)

a_set_comp = { n for n in range(21, 40) if n % 2 == 0}
print(a_set_comp)

# ( k ) A partir de la oración:
sent = 'Pack my box with five dozen liquor jugs'

sent_set = {n for n in sent.split() if len(n) > 3}
print(sent_set)

# (l) Usando comprehension, ¿cómo convertirías:
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# en:
# {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

d1_convert = {k.upper(): v*100 for k, v in d1.items() }
print(d1_convert)

# (n) ¿Cómo convertirías:
d2 = {'AMOL': 20, 'ANIL': 12, 'SUNIL': 13, 'RAMESH': 10}
# en:
# {'Amol': 400, 'Anil': 144, 'Sunil': 169, 'Ramesh': 100}
d2_convert = {k.capitalize(): v*v for k, v in d2.items() }
print(d2_convert)

# Pista: {k.capitalize(): v*v for k, v in d2.items()}

# (o) ¿Cómo convertirías las palabras presentes en una lista dada en
#     mayúsculas y las almacenarías en un set?
lst = ['Amol', 'Vijay', 'Vinay', 'Rahul', 'Sandeep']
lst_convert = {n.upper() for n in lst }
print(lst_convert)

# 15.10: Supón que un diccionario contiene pares clave-valor...
# Escribe un programa que obtenga los valores máximo y mínimo
# del diccionario usando max() y min() en combinación con lambda.

datos = {'a': 10, 'b': 3, 'c': 25, 'd': 1}


valor_max = max(datos.items(), key = lambda x: x[1])
valor_min = min(datos.items(), key = lambda x: x[1])

valor_max_final = max(datos.items(), key=lambda x: x[1])[1]
valor_min_final = min(datos.items(), key=lambda x: x[1])[1]

print(valor_max)
print(valor_min)
print(f"Máximo valor: {valor_max_final}")
print(f"Mínimo valor: {valor_min_final}")

