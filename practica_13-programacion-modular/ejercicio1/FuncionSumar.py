# import modulo_funcion_sumar
from modulo_funcion_sumar import sumar, restar, multiplicar, dividir

print('*** Operaciones Matemáticas ***')

# Definir valores
a = 8
b = 5

# Llamar a las funciones
resultado_suma = sumar(a, b)
resultado_resta = restar(a, b)
resultado_multiplicacion = multiplicar(a, b)
resultado_division = dividir(a, b)

# Mostrar resultados
print(f'Suma: {a} + {b} = {resultado_suma}')
print(f'Resta: {a} - {b} = {resultado_resta}')
print(f'Multiplicación: {a} × {b} = {resultado_multiplicacion}')
print(f'División: {a} ÷ {b} = {resultado_division}')

# print(__name__)
