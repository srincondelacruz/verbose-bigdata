
# Práctica 12: Tipos de Argumentos y Alcance (Scope)

Este documento cubre los diferentes tipos de argumentos en las funciones de Python (posicionales, keywords, `*args`, `**kwargs`, valores por defecto) y el concepto de alcance de variables (`global`).

---

## Sección 1: Argumentos Posicionales

Los argumentos posicionales son obligatorios y su orden importa.

### Ejercicio 1
Escribe una función llamada `calcular_area_rectangulo` que reciba dos argumentos posicionales: `base` y `altura`, y retorne el área del rectángulo.

```python
# Tu código aquí
Ejercicio 2
Crea una función presentar_persona que reciba tres argumentos posicionales: nombre, edad y ciudad, e imprima un mensaje como: "Hola, soy [nombre], tengo [edad] años y vivo en [ciudad]."

Python

# Tu código aquí
Ejercicio 3
Define una función dividir que reciba dos números (dividendo y divisor) y retorne el resultado de la división. Llama a la función con los valores en el orden correcto e incorrecto para observar qué sucede.

Python

# Tu código aquí
Sección 2: Argumentos por Palabras Clave (Keywords)
Permiten pasar argumentos especificando el nombre del parámetro, por lo que el orden no importa.

Ejercicio 4
Modifica el ejercicio 2 para llamar a la función presentar_persona usando argumentos por palabras clave en un orden diferente al de la definición.

Python

# Ejemplo: presentar_persona(ciudad='Madrid', nombre='Ana', edad=25)
# Tu código aquí
Ejercicio 5
Crea una función calcular_precio_final que reciba precio, descuento e impuesto. Llámala usando una combinación de argumentos posicionales y de palabras clave (recuerda que los posicionales deben ir primero).

Python

# Tu código aquí
Sección 3: Argumentos Posicionales Variables (*args)
Permite pasar un número variable de argumentos posicionales, que se empaquetan en una tupla.

Ejercicio 6
Escribe una función sumar_todos que use *args para recibir una cantidad variable de números y retorne su suma total.

Python

# Debe funcionar con: sumar_todos(1, 2, 3) → 6
# Y también con: sumar_todos(10, 20, 30, 40, 50) → 150
# Tu código aquí
Ejercicio 7
Crea una función encontrar_maximo que use *args para recibir varios números y retorne el mayor de todos. No uses la función max() de Python, implementa tu propia lógica.

Python

# Tu código aquí
Sección 4: Argumentos de Palabra Clave Variables (**kwargs)
Permite pasar un número variable de argumentos nombrados (keyword), que se empaquetan en un diccionario.

Ejercicio 8
Define una función mostrar_datos_producto que use **kwargs para recibir información sobre un producto (nombre, precio, stock, categoría, etc.) e imprima cada dato en una línea separada con formato: "clave: valor".

Python

# Ejemplo de llamada:
# mostrar_datos_producto(nombre='Laptop', precio=899.99, stock=15, marca='Dell')
# Tu código aquí
Ejercicio 9
Crea una función crear_perfil que use **kwargs para crear un diccionario con datos de usuario y lo retorne. Luego llama a la función con diferentes cantidades de argumentos.

Python

# Tu código aquí
Sección 5: Combinando Todo
El orden de definición debe ser: posicionales, *args, keywords_obligatorios, **kwargs.

Ejercicio 10
Escribe una función procesar_pedido que reciba:

Un argumento posicional: numero_pedido

Argumentos posicionales variables: *productos (nombres de productos)

Dos argumentos de palabra clave obligatorios: cliente y direccion

Argumentos de palabra clave variables: **opciones_envio

La función debe imprimir toda la información del pedido de forma organizada.

Python

# Tu código aquí
Ejercicio 11
Crea una función calcular_estadisticas que reciba números como *args y retorne un diccionario con: suma, promedio, minimo y maximo de esos números.

Python

# Tu código aquí
Sección 6: Argumentos con Valores Predeterminados
Permiten que un argumento sea opcional. Deben ir después de los argumentos sin valor por defecto.

Ejercicio 12
Define una función saludar con tres parámetros: nombre (sin valor por defecto), saludo (valor por defecto: "Hola") y puntuacion (valor por defecto: "!"). Prueba llamarla de diferentes formas: solo con nombre, con nombre y saludo, y con los tres argumentos.

Python

# Tu código aquí
Ejercicio 13
Crea una función calcular_descuento que reciba precio (sin valor por defecto) y porcentaje_descuento (valor por defecto: 10). La función debe retornar el precio final después del descuento.

Python

# Tu código aquí
Sección 7: Alcance de Variables (Scope)
Define dónde es accesible una variable.

Ejercicio 14
Observa y predice qué imprimirá el siguiente código ANTES de ejecutarlo. Luego ejecútalo y explica el resultado:

Python

contador = 0

def incrementar():
    contador = contador + 1
    return contador

print(incrementar())
print(contador)
Preguntas:

¿Por qué ocurre un error (UnboundLocalError)?

¿Cómo lo solucionarías usando global?

Ejercicio 15
Crea un programa con:

Una variable global saldo = 1000

Una función depositar(cantidad) que añada dinero al saldo

Una función retirar(cantidad) que reste dinero del saldo

Una función mostrar_saldo() que imprima el saldo actual

Asegúrate de usar correctamente la palabra clave global donde sea necesario.

Python

# Tu código aquí