# Parte 01 - Comprehensions

## ¿Qué son las comprehensions?

> 💡
>
> Las comprehensions ofrecen una forma fácil y compacta de crear listas, conjuntos y diccionarios.
> Una comprehension funciona recorriendo o iterando sobre elementos y asignándolos a un contenedor como lista, conjunto o diccionario.
> Este contenedor no puede ser una tupla, ya que al ser inmutable no puede recibir asignaciones.

## List Comprehension (Comprensión de listas)

Una comprensión de lista consiste en corchetes que contienen una expresión seguida de una cláusula `for`, y cero o más cláusulas `for` o `if`.

La forma general de una comprensión de lista es:
`lst = [expresión for var in secuencia [opcional for and/or if]]`

A continuación se presenta un diagrama con la transformación de la estructura clásica en listas por comprensión:
*(Diagrama omitido)*

### Ejemplos de list comprehension:

Generar 20 números aleatorios en el rango de 10 a 100:
```python
import random
a = [random.randint(10, 100) for n in range(20)]
# [63, 19, 53, 95, 84, 37, 22, 32, 67, 34, 93, 35, 20, 97, 35, 49, 62, 51, 93, 15]
Generar cuadrado y cubo de todos los números entre 0 y 10:

Python

a = [(x, x**2, x**3) for x in range(10)]
print(a)
# [(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729)]
Convertir una lista de strings a una lista de enteros:

Python

a = [int(x) for x in ['10', '20', '30', '40']]
print(a)
# [10, 20, 30, 40]
Ejemplos del uso de if en list comprehension:
Generar una lista de números pares en el rango de 10 a 30:

Python

a = [n for n in range(10, 30) if n % 2 == 0]
print(a)
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
De una lista, eliminar todos los números con valor entre 20 y 50:

Python

# (Asumiendo que 'a' es la lista anterior)
a = [num for num in a if num < 20 or num > 50]
print(a)
# [10, 12, 14, 16, 18]
Ejemplo del uso de if-else en list comprehension:
Nota: Cuando se usan if-else, se colocan antes del for.

Reemplazar una vocal en una cadena con !:

Python

a = ['!' if alphabet in 'aeiou' else alphabet for alphabet in 'Technical']
print(a)
# ['T', '!', 'c', 'h', 'n', '!', 'c', '!', 'l']
Ejemplo del uso de múltiples for y if
Aplanar una lista de listas (dos formas):

Python

arr = [[1,2,3,4], [5,6,7,8], [10, 11, 12, 13]]

# Forma 1: for anidado
b = [n for ele in arr for n in ele]
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13]

# Forma 2: Desempaquetado con *
c = [*arr[0], *arr[1], *arr[2]]
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13]
Nota la diferencia entre for anidado y comprensión anidada:

Python

# Produce [4, 5, 6, 5, 6, 7, 6, 7, 8]. Usa for anidado
lst = [a + b for a in [1, 2, 3] for b in [3, 4, 5]]
print(lst)

# Produce [[4, 5, 6], [5, 6, 7], [6, 7, 8]]. Usa comprensión anidada
lst = [[a + b for a in [1, 2, 3]] for b in [3, 4, 5]]
print(lst)
Generar todas las combinaciones únicas de 1, 2 y 3:

Python

a = [(i, j, k) for i in [1,2,3] for j in [1,2,3] for k in [1, 2, 3] if i != j and j != k and k != i]
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
🔹 Set Comprehension (Comprensión de conjuntos)
Al igual que las list comprehensions, las set comprehensions ofrecen una forma fácil de crear conjuntos. Consisten en llaves {} que contienen una expresión seguida de una cláusula for, y opcionalmente más for o if.

Sintaxis general: s = {expresión for var in secuencia [if condición] [for ...]}

✅ Ejemplos de set comprehension
Generar un conjunto con los cuadrados de números del 0 al 9:

Python

a = {x**2 for x in range(10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
De un conjunto, eliminar todos los números entre 20 y 50:

Python

a = {num for num in a if num > 20 and num < 50}
# {49, 36, 25}
🔹 Dictionary Comprehension (Comprensión de diccionarios)
Permite crear diccionarios de forma compacta a partir de iterables. Usa llaves {} y la sintaxis: {clave: valor for (clave, valor) in iterable}

Sintaxis General: dict_var = {clave: valor for (clave, valor) in diccionario.items()}

✅ Ejemplos de dictionary comprehension
Diccionario inicial:

Python

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Obtener diccionario con cada valor al cubo:

Python

d1 = {k: v ** 3 for (k, v) in d.items()}
print(d1)
# {'a': 1, 'b': 8, 'c': 27, 'd': 64}
Solo los valores mayores a 3, al cubo:

Python

d2 = {k: v ** 3 for (k, v) in d.items() if v > 3}
print(d2)
# {'d': 64}
Identificar entradas pares e impares:

Python

d3 = {k: ('Even' if v % 2 == 0 else 'Odd') for (k, v) in d.items()}
print(d3)
# {'a': 'Odd', 'b': 'Even', 'c': 'Odd', 'd': 'Even'}
Parte 02 - Programación Funcional
💡 En la programación funcional, un problema se trata como la evaluación de una o más funciones. Por lo tanto, un problema dado se descompone en un conjunto de funciones. Estas funciones proporcionan la principal fuente de lógica en el programa.

Funciones como Valores de Primera Clase
Python facilita la programación funcional al tratar las funciones como valores de datos "de primera clase". Esto significa que:

Las funciones pueden asignarse a variables.

Las funciones pueden pasarse como argumentos a otras funciones.

Las funciones pueden ser devueltas por otras funciones.

Las funciones pueden construirse en tiempo de ejecución.

Ejemplo: Asignar a variable
Python

def saludar():
    print("¡Hola!")

# Asignamos la función a una variable
mi_funcion = saludar
mi_funcion() # Nota: se llama a mi_funcion(), no a saludar()
# Salida: ¡Hola!
Ejemplo: Pasar como argumento
Python

def aplicar(funcion, valor):
    return funcion(valor)

def cuadrado(x):
    return x * x

# Pasamos la función cuadrado como argumento
resultado = aplicar(cuadrado, 5)
# Salida: 25
Ejemplo: Devolver una función
Python

def crear_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

duplicar = crear_multiplicador(2)
print(duplicar(10)) # Salida: 20

triplicar = crear_multiplicador(3)
print(triplicar(30)) # Salida: 90
Ejemplo: Construir en tiempo de ejecución
Python

def construir_funcion_operacion(operador):
    def sumar(x, y):
        return x + y
    def restar(x, y):
        return x - y

    if operador == 'sumar':
        return sumar
    elif operador == 'restar':
        return restar
    else:
        raise ValueError("Operador no soportado")

operacion = construir_funcion_operacion('restar')
print(operacion(10, 4)) # Salida: 6
Funciones Lambda
💡

Las funciones normales tienen nombre (def).

Las funciones lambda son funciones anónimas o en línea.

Se usan para funciones cortas que es conveniente definir en el punto en que se llaman.

Pueden recibir cualquier número de argumentos, pero sólo pueden tener una expresión.

Ejemplos de Lambda
Función que calcula el cubo de un número:

Python

# Con def
def cubo(a):
    return a**3

# Con lambda
cubo = lambda a: a**3
print(cubo(8)) # Salida: 512
Función que calcula el promedio de 3 argumentos:

Python

# Con def
def promedio(x, y, z):
    return (x + y + z) / 3

# Con lambda
promedio = lambda x, y, z: (x + y + z) / 3
print(promedio(2, 4, 11)) # Salida: 5.666...
Función que recibe nombre y apellido:

Python

# Con lambda
nomb_comp = lambda Nombre, Apellido: f'El nombre completo es: {Nombre} {Apellido}'
t = nomb_comp('Nicolás', 'Pérez')
print(t) # Salida: El nombre completo es: Nicolás Pérez
Lambdas pasadas directamente a print():

Python

print((lambda a: a**3)(8)) # Salida: 512
print((lambda x, y, z: (x + y + z) / 3)(2, 4, 11)) # Salida: 5.666...
Lambdas con contenedores (listas, tuplas):

Python

lista_1 = [1, 2, 3, 4, 5]
print((lambda L1: sum(L1)/len(L1))(lista_1)) # Salida: 3.0
Funciones de Orden Superior
Una función de orden superior es una función que puede recibir otras funciones como argumentos o devolverlos.

Ejemplo con def:
Python

def incrementar(x):
    return x + 1

def func_orden_sup(x, func):
    return x + func(x)

resultado = func_orden_sup(2, incrementar) # 2 + (2 + 1)
print(resultado) # Salida: 5
Ejemplo con lambda:
Python

incrementar = lambda x: x + 1
func_orden_sup = lambda x, func: x + func(x)
resultado = func_orden_sup(2, incrementar)
print(resultado) # Salida: 5
Ejemplo: sorted() con lambda
El uso más común: lambda como argumento key.

Python

d = {'Aceite': 230, 'Pan': 150, 'Salmón': 175, 'Jamón': 35}
# Ordenar por valor (índice 1 de la tupla)
d1 = sorted(d.items(), key = lambda a: a[1])
print(d1)
# Salida: [('Jamón', 35), ('Pan', 150), ('Salmón', 175), ('Aceite', 230)]
Funciones map(), filter() y reduce()
Para facilitar la programación funcional, Python proporciona 3 funciones de orden superior:

map(): Transformar
Su objetivo es aplicar una función (transformación) a cada elemento de un iterable.

Sintaxis: map(funcion, iterable)

Ejemplo: Duplicar números

Python

# Sin map
numeros = [1, 2, 3, 4]
numeros_2 = []
for i in numeros:
    numeros_2.append(i * 2)
# Salida: [2, 4, 6, 8]

# Con map() y lambda
numeros = [1, 2, 3, 4]
numeros_3 = list(map(lambda i: i*2, numeros))
print(numeros_3) # Salida: [2, 4, 6, 8]
Ejemplo: Sumar dos listas

Python

numeros_4 = [1, 2, 3, 4]
numeros_5 = [5, 6, 7]
resultado = list(map(lambda x, y: x + y, numeros_4, numeros_5))
print(resultado) # Salida: [6, 8, 10] (Para en la lista más corta)
Ejemplo: Extraer precios de diccionarios

Python

items = [
    {'producto': 'camisa', 'precio': 100},
    {'producto': 'pantalones', 'precio': 300},
]
precios = list(map(lambda item: item['precio'], items))
print(precios) # Salida: [100, 300]
Ejemplo: map con def (para lógica compleja)

Python

def añadir_impuestos(item):
    item['impuestos'] = item['precio'] * .15
    return item

new_items = list(map(añadir_impuestos, items))
# Salida: [{'producto': 'camisa', 'precio': 100, 'impuestos': 15.0}, ...]
filter(): Filtrar
Selecciona elementos de una lista si cumplen una condición (la función devuelve True).

Sintaxis: filter(funcion, iterable)

Ejemplo: Filtrar números pares

Python

# Sin filter
numbers = [1, 2, 3, 4, 5]
new_numbers = []
for numero in numbers:
    if numero % 2 == 0:
        new_numbers.append(numero)
# Salida: [2, 4]

# Con filter() y lambda
numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers) # Salida: [2, 4]
Ejemplo: Filtrar diccionarios

Python

matches = [
    {'home_team': 'España', 'home_team_result': 'Win'},
    {'home_team': 'Francia', 'home_team_result': 'Draw'},
    {'home_team': 'Portugal', 'home_team_result': 'Win'},
]
# Filtrar solo los que ganaron
new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(len(new_list)) # Salida: 2
Ejemplo: filter con def

Python

def fun(n):
    return n % 5 == 0

lst2 = [5, 10, 18, 27, 25]
f2 = filter(fun, lst2)
print(list(f2)) # Salida: [5, 10, 25]
reduce(): Reducir
Aplica una función acumulativa a una secuencia para reducirla a un solo valor.

Sintaxis:

Python

from functools import reduce
reduce(funcion_de_dos_args, iterable[, valor_inicial])
Ejemplo: Suma acumulada

Python

import functools
numbers = [1, 2, 3, 4]

# La lambda toma el acumulador (counter) y el item actual
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result) # Salida: 10
Tabla de ejecución (Suma): | Iteration | Counter | Item | Return | | :---: | :---: | :---: | :---: | | 1 | 0 (valor inicial por defecto) | 1 | 1 | | 2 | 1 | 2 | 3 | | 3 | 3 | 3 | 6 | | 4 | 6 | 4 | 10 |

Ejemplo: reduce con diccionarios (y valor_inicial=0)

Python

import functools
items = [
    {'producto': 'camisa', 'precio': 100},
    {'producto': 'pantalones', 'precio': 300},
    {'producto': 'pantalones 2', 'precio': 200}
]

def accum(counter, item):
    print(f'counter => {counter}, item => {item["precio"]}')
    return counter + item['precio']

# Usamos 0 como valor_inicial para el counter
total = functools.reduce(accum, items, 0)
print(total) # Salida: 600
Tabla de ejecución (Diccionarios): | Iteration | Counter (Acumulador) | Item (Actual) | Return (Nuevo Acumulador) | | :---: | :---: | :---: | :---: | | 1 | 0 (valor inicial) | {'precio': 100} | 100 | | 2 | 100 | {'precio': 300} | 400 | | 3 | 400 | {'precio': 200} | 600 |

Uso de map/filter/reduce en Bases de Datos
Las bases de datos relacionales usan este paradigma. Una consulta SQL: SELECT max(salary) FROM Employees WHERE grade = 'Skilled'

...es conceptualmente lo mismo que: reduce(max, map(get_salary, filter(lambda x: x.grade == 'Skilled', employees)))
